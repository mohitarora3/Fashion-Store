from flask import render_template, redirect, url_for, Blueprint, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from ecommerce.users.forms import RequestResetForm, ResetPasswordForm, RegistrationForm, LoginForm, DeliveryForm
from ecommerce.users.utils import send_reset_email
from ecommerce import db, bcrypt, mongo
from ecommerce.models import User
import json
from bson.objectid import ObjectId

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.objects(email=form.email.data).first()
        if existing_user is None:
            hashpass = generate_password_hash(form.password.data, method='sha256')
            hey = User(form.username.data, form.email.data, hashpass).save()
            flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.objects(email=form.email.data).first()
        if check_user and check_password_hash(check_user['password'], form.password.data):
            login_user(check_user)
            flash('You have been successfully logged in', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/saving/<string:item_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(item_id):
    id = current_user.get_id()
    item = mongo.db.user.find_one({'_id': ObjectId(id), 'item.item_id': item_id, 'item.size': request.form['si']})
    if item is None:
        a = {"item_id": item_id, "size": request.form['si'], "quantity": 1}
        mongo.db.user.update_one(
            {"_id": ObjectId(id)
             },
            {"$push":
             {"item": a
              }
             }
        )
        flash('This item has been successfully added to cart', 'success')
    else:
        flash('This item is already present in your cart', 'success')
    return redirect(url_for('main.home'))


@users.route('/updating/<string:item_id>/<string:item_attr>', methods=['GET', 'POST'])
@login_required
def update_cart(item_id, item_attr):
    id = current_user.get_id()
    # item=mongo.db.items.find_one({'_id': ObjectId(item_id)}, {"_id": 0, "Size": 1})
    # size=item["Size"]
    if('qt' in request.form):
        mongo.db.user.update_one(
            {"_id": ObjectId(id),
             "item.item_id": item_id,
             "item.size": item_attr
             },
            {"$set":
             {"item.$.quantity": request.form['qt']}
             }
        )
    elif('si' in request.form):
        mongo.db.user.update_one(
            {"_id": ObjectId(id),
             "item.item_id": item_id,
             "item.quantity": item_attr
             },
            {"$set":
                {"item.$.size": request.form['si']}
             }
        )
    return redirect(url_for('users.cart'))


@users.route('/removing/<string:item_id>,<string:size>', methods=['GET', 'POST'])
@login_required
def remove_from_cart(item_id, size):
    id = current_user.get_id()
    mongo.db.user.update_one(
        {"_id": ObjectId(id),
         },
        {"$pull":
            {"item":
                {
                    "item_id": item_id,
                    "size": size
                }
             }
         }
    )
    flash('Successfully Removed', 'success')
    return redirect(url_for('users.cart'))


def cart_details(id):
    Items = mongo.db.user.find_one(
        {"_id": ObjectId(id)
         },
        {
            "_id": 0, "item": 1
        }
    )
    if Items:
        lst = []
        dict = {}
        bag_mrp = 0
        bag_price = 0
        Items = Items['item']
        number_of_items = len(Items)
        for item in Items:
            id = item['item_id']
            size = item['size']
            quantity = int(item['quantity'])
            for a in mongo.db.items.find({'_id': ObjectId(id)}):
                a['quantity'] = quantity
                a['size'] = size
                bag_mrp += quantity * a['Mrp']
                bag_price += quantity * a['Price']
                lst.append(a)
        dict['bag_discount'] = bag_mrp - bag_price
        dict['bag_mrp'] = bag_mrp
        dict['bag_total'] = bag_price
        return lst, dict, number_of_items


@users.route('/my_cart', methods=['GET', 'POST'])
@login_required
def cart():
    id = current_user.get_id()
    cart_status = mongo.db.user.find({'$and': [{'_id': ObjectId(id)}, {'item': {'$exists': 'true'}}]}).count()
    if cart_status:
        lst, dict, number_of_items = cart_details(id)
        return render_template('cart.html', items=lst, dict=dict, number=number_of_items)
    else:
        return render_template('cart.html', number=0)


@users.route('/checkout/address')
@login_required
def checkout():
    id = current_user.get_id()
    count = mongo.db.user.find({'$and': [{'_id': ObjectId(id)}, {'list_address': {'$exists': 'true'}}]}).count()
    if count == 0:
        return redirect(url_for('users.address'))
    else:
        lst, dict, number_of_items = cart_details(id)
        address = mongo.db.user.find_one({'_id': ObjectId(id)}, {'_id': 0, 'list_address': 1})
        return render_template('checkout.html', list_address=address['list_address'], lst=lst, dict=dict, number=number_of_items)


@users.route('/checkout/place_order', methods=['GET', 'POST'])
@login_required
def place_order():
    lst_items=[]
    id = current_user.get_id()
    number = int(request.form['address_number'])
    dict_items_info = mongo.db.user.find_one({'_id': ObjectId(id)}, {'_id': 0, 'item': 1, 'list_address': 1})
    lst_items_info = dict_items_info['item']
    lst_address_details = dict_items_info['list_address']
    for item_info in lst_items_info:
        item_size = 'Size.' + item_info['size']
        mongo.db.items.update_one({'_id': ObjectId(item_info['item_id'])},
                                  {'$inc':
                                   {item_size: -int(item_info['quantity'])
                                    }
                                   }
                                  )
        item=mongo.db.items.find_one({'_id':ObjectId(item_info['item_id'])},{'_id':0,'Mrp':1,'Discount':1})
        item_info['mrp']=item['Mrp']
        item_info['discount']=item['Discount']
        lst_items.append(item_info)
    mongo.db.order.insert_one({'user_id': id, 'item_details': lst_items, 'delivery_details': lst_address_details[number]})
    mongo.db.user.update_one({'_id': ObjectId(id)}, {'$unset': {'item': 1}})
    return render_template('order_placed.html', title='Order Placed')


@users.route('/user/address', methods=['GET', 'POST'])
@login_required
def address():
    form = DeliveryForm()
    if form.validate_on_submit():
        id = current_user.get_id()
        a = {'name': form.name.data, 'address': form.address.data, 'state': form.state.data, 'city': form.city.data, 'pin_code': form.pin_code.data, 'phone_number': form.phone_number.data}
        mongo.db.user.update_one(
            {
                '_id': ObjectId(id)
            },
            {
                '$push':
                {'list_address': a

                 }
            }
        )
        flash('Your address has been saved', 'success')
        return redirect(url_for('users.checkout'))
    return render_template('address.html', form=form, title='address')


@users.route('/user/address/remove/<string:number>')
@login_required
def remove_address(number):
    id = current_user.get_id()
    list_address_number = 'list_address.' + number
    mongo.db.user.update_one(
        {"_id": ObjectId(id)
         },
        {"$unset":
            {list_address_number: 1
             }
         }
    )
    mongo.db.user.update_one({'_id': ObjectId(id)},
                             {'$pull':
                              {
                                  'list_address': 'Null'
                              }
                              }
                             )
    return redirect(url_for('users.checkout'))


@users.route('/user/address/update')
@login_required
def update_address(address):
    id = current_user.get_id()
    mongo.db.user.update_one(
        {"_id": ObjectId(id)
         },
        {"$pull":
            {"list_address": address
             }
         }
    )
    return redirect(url_for('users.address'))


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.objects(email=form.email.data).first()
            if user is None:
                flash('There is no account with this email.', 'danger')
                return redirect(url_for('users.reset_request'))
            send_reset_email(user)
            flash('An email has been sent with instructions to rest your password', 'success')
            return redirect(url_for('users.login'))
        return render_template('reset_request.html', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated():
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is an invalid or expired token', 'danger')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashpass = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
        db.session.commit()
        flash('Your password has benn updated!', 'success')
        redirect(url_for('login'))

    return render_template('reset_token.html', form=form)
