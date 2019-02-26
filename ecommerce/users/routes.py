<<<<<<< HEAD
import math
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, Blueprint, flash, request,  redirect, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from ecommerce.users.forms import RequestResetForm, ResetPasswordForm, RegistrationForm, LoginForm, DeliveryForm, ReviewForm
from ecommerce.seller.forms import ItemForm
from ecommerce.users.utils import send_reset_email
from ecommerce import  db,bcrypt, mongo
=======
import math,string,secrets
import flask_admin as admin
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, Blueprint, flash, request, redirect, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user
from ecommerce.users.forms import RequestResetForm, ResetPasswordForm, RegistrationForm, LoginForm, DeliveryForm, ReviewForm
from ecommerce.seller.forms import SellerForm
from ecommerce.seller.forms import ItemForm
from ecommerce.users.utils import send_reset_email, sendPasswordSeller
from ecommerce import db, bcrypt, mongo
>>>>>>> upstream/master
from ecommerce.models import User
import json
from bson.objectid import ObjectId
import os
<<<<<<< HEAD
from flask_pymongo import PyMongo
=======
from functools import wraps
from bson.json_util import dumps


>>>>>>> upstream/master

users = Blueprint('users', __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


<<<<<<< HEAD

=======
>>>>>>> upstream/master
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.objects(email=form.email.data).first()
        if existing_user is None:
<<<<<<< HEAD
            hashpass = generate_password_hash(form.password.data, method='sha256')
            a='customer'
            if form.seller.data:
                a='seller'
            hey = User(form.username.data, form.email.data,hashpass,a).save()
=======
            hashpass = generate_password_hash(form.password.data,method='sha256')
            role = 'customer'
            if form.seller.data:
                role= 'seller'
                approved=0
                User(form.username.data, form.email.data, hashpass,role,approved).save()
                flash('Your registeration is successfull.', 'success')
                form=SellerForm()
                if(form.validate_on_submit()):
                    return render_template('registration(part-3).html',title='Completed')
                return render_template('seller_registration.html',title='Step 2',form=form)
                    
            else:
                User(form.username.data, form.email.data, hashpass,role).save()


>>>>>>> upstream/master

            flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register', form=form)

<<<<<<< HEAD
=======

def roles_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    id = current_user.get_id()
    print('user id : ', id)
    user= mongo.db.user.find_one({"_id": ObjectId(id)})
    print(user)
    print(user['email'], " ", user['role'])
    if user['role'] == 'customer' or user['role']=='seller':
      flash('You are not an admin')
      return render_template('errors/403.html'), 403


    return f(*args, **kwargs)
  return decorated_function


>>>>>>> upstream/master
@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = User.objects(email=form.email.data).first()
        if check_user and check_password_hash(check_user['password'], form.password.data):
            login_user(check_user)
<<<<<<< HEAD
=======
            #id = current_user.get_id()
            #user_document=mongo.db.user.find_one({'_id':ObjectId(id)},{'_id':0,'role':1})
            #if user_document['role']=='admin':
             #   return redirect('/admin_')
>>>>>>> upstream/master
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

<<<<<<< HEAD

=======
@users.route('/admin_')
@login_required
@roles_required
def admin():
    #Admin = admin(current_app)

    print(current_user.get_id())
    print("yessssssssssssssssssssssssssssss")
    approvedSellers=mongo.db.user.find({'role':'seller','approved':True})
    unapprovedSellers=mongo.db.user.find({'role':'seller','approved':False})
    
    return render_template('admin_portal.html',title='Admin portal',approvedSellers=approvedSellers,unapprovedSellers=unapprovedSellers)


@users.route('/seller/approved/<string:seller_id>', methods=['POST'])

# @login_required
# @roles_required
def seller_approved(seller_id):
    #Admin = admin(current_app)

    print(seller_id)
    print("nnnnnnnssssssssssssssssssssssssssssss")
    # generating password to be sent to seller that contains atleast 1 lowercase, uppercase, digit, punctiation
    passwordSource= string.ascii_letters +string.digits +string.punctuation
    password= secrets.choice(string.ascii_lowercase)
    password+=secrets.choice(string.ascii_uppercase)
    password+=secrets.choice(string.digits)
    password+=secrets.choice(string.punctuation)
    print('Data')    
    for i in range(0,6):
        password+=secrets.choice(passwordSource)
    hashpass = generate_password_hash(password,method='sha256')
    sellerDocument=mongo.db.user.find_one({'_id':ObjectId(seller_id)},{'_id':0,'email':1})

    #sending password to seller 
    #sendPasswordSeller(sellerDocument['email'],password)
    print('is')
    '''
    mongo.db.user.update_one({'_id':ObjectId(seller_id)},
        {
        '$set':
            {
                'approved':True,
                'password':hashpass,

            }
        })
    '''
    print('here')
    sellers=mongo.db.user.find({'role':'seller', 'approved':False})
    sellersJson=dumps(sellers)
    return sellersJson


    






@users.route('/add_wishlist/<string:item_id>', methods=['GET', 'POST'])
@login_required
def add_to_wishlist(item_id):
    id = current_user.get_id()
    item = mongo.db.user.find({'_id': ObjectId(id), 'wishlist.item_id': ObjectId(item_id)}).count()
    if item == 0:
        itemdetail = mongo.db.items.find_one({'_id': ObjectId(item_id)})
        a = {"item_id": ObjectId(item_id)}
        mongo.db.user.update_one(
            {"_id": ObjectId(id)
             },
            {"$push":
             {"wishlist": a
              }
             }
        )
        flash('This item has been successfully added to yor wishlist', 'success')
    else:
        flash('This item is already present in your wishlist', 'success')
    return redirect(url_for('main.home'))


@users.route('/removing/<string:item_id>', methods=['GET', 'POST'])
@login_required
def remove_from_wishlist(item_id):
    id = current_user.get_id()
    mongo.db.user.update_one(
        {"_id": ObjectId(id),
         },
        {"$pull":
            {"wishlist":
                {
                    "item_id": ObjectId(item_id),
                }
             }
         }
    )
    flash('Successfully Removed', 'success')
    return redirect(url_for('users.wishlist'))

@users.route('/my_wishlist', methods=['GET', 'POST'])
@login_required
def wishlist():
    id = current_user.get_id()
    result_cursor = mongo.db.user.aggregate([{'$match': {'_id': ObjectId(id)}},
                                  {'$project':
                                   {'_id': 0, 'wishlist': 1, 'count':
                                    {'$size': '$wishlist'}
                                    }
                                   }
                                  ])
    for result in result_cursor:
        if result['count']>0:
            count=result['count']
            print(count)
            items = mongo.db.user.aggregate([
                {'$match': {'_id': ObjectId(id)}},
                {'$lookup':
                 {
                     'from': 'items',
                     'localField': 'wishlist.item_id',
                     'foreignField': '_id',
                     'as': 'item_info'
                 }
                 },
                {'$project': {'_id':0,'item_info.Category':1,'item_info._id': 1, 'item_info.Type': 1, 'item_info.Category': 1, 'item_info.Color': 1, 'item_info.Seller': 1, 'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1, "item_info.Price":1,"item_info.Discount":1},
                 }
            ])
            break
        else:
            count=0
            items=None
            print(count)
            break
    if(items):
        for item in items:
            items=item["item_info"]
    else:
        items=None
    return render_template('wishlist.html',items_dict=items,count=count)
>>>>>>> upstream/master
@users.route('/saving/<string:item_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(item_id):
    id = current_user.get_id()
    item = mongo.db.user.find({'_id': ObjectId(id), 'item.item_id': ObjectId(item_id), 'item.size': request.form['si']}).count()
    if item==0:
<<<<<<< HEAD
        itemdetail=mongo.db.items.find_one({'_id':ObjectId(item_id)})
        a = {"item_id":ObjectId(item_id), "size": request.form['si'], "quantity": 1,"SellerId":itemdetail['SellerId']}
=======
        print(request.form['si'])
        itemdetail=mongo.db.items.find_one({'_id':ObjectId(item_id)})
        #this comment is to be removed on using with mlab (online databse)
        #a = {"item_id":ObjectId(item_id), "size": request.form['si'], "quantity": 1,"SellerId":itemdetail['SellerId']}
        a = {"item_id":ObjectId(item_id), "size": request.form['si'], "quantity": 1}
       
>>>>>>> upstream/master
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
<<<<<<< HEAD
    if('qt' in request.form):
        mongo.db.user.update_one(
            {"_id": ObjectId(id),
             "item.item_id": ObjectId(item_id),
             "item.size": item_attr
             },
=======
    print(item_id)
    print('nefjef')
    print(item_attr)
    print(type(item_attr))
    if('qt' in request.form):
        mongo.db.user.update_one(
            {
                        "_id": ObjectId(id),
                        "item":
                                {"$elemMatch":
                                {"item_id": ObjectId(item_id),
                                "size": item_attr
                                }
                    }
                },
>>>>>>> upstream/master
            {"$set":
             {"item.$.quantity": int(request.form['qt'])}
             }
        )
    elif('si' in request.form):
        mongo.db.user.update_one(
            {"_id": ObjectId(id),
             "item.item_id": ObjectId(item_id),
             "item.quantity": int(item_attr)
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
                    "item_id": ObjectId(item_id),
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
<<<<<<< HEAD
=======
        if bag_price>=1499:
            if bag_price>=2999:
                offer_discount=bag_price*0.1+bag_price*0.05
            else:
                offer_discount=bag_price*0.1
        else:
            offer_discount=0
        dict['bag_offer_discount']=round(offer_discount,2)
        if bag_price<999:
            dict['delivery']=149
        else:
            dict['delivery']=0
        dict['tax']=round(0.05*bag_price,2)
        dict['order_total']=int(dict['tax']+dict['delivery']+bag_price-offer_discount)
>>>>>>> upstream/master
        return lst, dict, number_of_items


@users.route('/my_cart', methods=['GET', 'POST'])
<<<<<<< HEAD
@login_required
=======

>>>>>>> upstream/master
def cart():
    id = current_user.get_id()
    cart_status = mongo.db.user.find({'$and': [{'_id': ObjectId(id)}, {'item': {'$exists': 'true'}}]}).count()
    if cart_status:
        lst, dict, number_of_items = cart_details(id)
        return render_template('cart.html', items=lst, dict=dict, number=number_of_items)
    else:
        return render_template('cart.html', number=0)


@users.route('/checkout/address')
<<<<<<< HEAD
@login_required
=======

>>>>>>> upstream/master
def checkout():
    id = current_user.get_id()
    count = mongo.db.user.find({'$and': [{'_id': ObjectId(id)}, {'list_address': {'$exists': 'true'}}]}).count()
    if count == 0:
        return redirect(url_for('users.address'))
    else:
        lst, dict, number_of_items = cart_details(id)
        address = mongo.db.user.find_one({'_id': ObjectId(id)}, {'_id': 0, 'list_address': 1})
        return render_template('checkout.html', list_address=address['list_address'], lst=lst, dict=dict, number=number_of_items, delivery_date=
            datetime.now()+timedelta(days=7))


@users.route('/checkout/place_order', methods=['GET', 'POST'])
<<<<<<< HEAD
@login_required
=======
>>>>>>> upstream/master
def place_order():
    lst_items=[]
    price=0
    order_total=0
<<<<<<< HEAD
    id = current_user.get_id()
=======
    status="IN PROGRESS"
    id = current_user.get_id()
    _, dict, number_of_items = cart_details(id)

>>>>>>> upstream/master
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
        item=mongo.db.items.find_one({'_id':item_info['item_id']},{'_id':0,'Mrp':1,'Discount':1})
<<<<<<< HEAD
        #item_info['mrp']=item['Mrp']
        #item_info['discount']=item['Discount']
        price=item['Mrp']-item['Mrp']*item['Discount']/100
        item_info['price']=price*int(item_info['quantity'])
        order_total+=price+int(item_info['quantity'])
        lst_items.append(item_info)
    order_total=math.floor(order_total)
    mongo.db.order.insert_one({'date': datetime.now(), 'delivery_date':datetime.now() +timedelta(days=7),'user_id': id, 'item_details': lst_items,'delivery_details': lst_address_details[number], 'order_total':order_total, 'status':'IN PROGRESS'})
=======
        item_info['mrp']=item['Mrp']
        item_info['discount']=item['Discount']
        price=item['Mrp']-item['Mrp']*item['Discount']/100
        item_info['price']=price*int(item_info['quantity'])
        item_info['status']=status
        order_total+=price+int(item_info['quantity'])
        lst_items.append(item_info)
    order_total=math.floor(order_total)
    mongo.db.order.insert_one({'date': datetime.now(), 'delivery_date':datetime.now() +timedelta(days=7),'user_id': id, 'item_details': lst_items,'status':'IN PROGRESS','delivery_details': lst_address_details[number], 'order_info':dict})
>>>>>>> upstream/master
    mongo.db.user.update_one({'_id': ObjectId(id)}, {'$unset': {'item': 1}})
    return render_template('order_placed.html', title='Order Placed')

@users.route('/my_orders/')
<<<<<<< HEAD
@login_required
def orders():
    id=current_user.get_id()
    user_orders=mongo.db.order.find({'user_id':id})
    for user_order in user_orders:
        if user_order['status']=='IN PROGRESS':
            current_date=datetime.now().date()
            if current_date >= user_order["delivery_date"].date():
                mongo.db.order.update_one({'_id':user_order['_id']},{'$set':{'status':'DELIVERED'}})
=======

def orders():
    id = current_user.get_id()
    user_orders=mongo.db.order.find({'user_id':id})
    for user_order in user_orders:
        item_details=user_order['item_details']
        for item_detail in item_details:
            if item_detail['status']=='IN PROGRESS':
                    current_date=datetime.now().date()
                    if current_date >= user_order["delivery_date"].date():
                        mongo.db.order.update_one({'_id':user_order['_id'],'item_details.item_id':item_detail['item_id'],'item_details.size':item_detail['size']},{'$set':{'status':'DELIVERED'}})
>>>>>>> upstream/master
    dict_order_details= mongo.db.order.aggregate([
    {'$match': {'user_id': id}},
    {'$lookup':
     {
         'from': 'items',
         'localField': 'item_details.item_id',
         'foreignField': '_id',
         'as': 'item_info'
     }
     },
<<<<<<< HEAD
    {'$project': {'item_info._id': 1, 'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1, 'item_details.price': 1,  'item_details.quantity': 1, 'item_details.size':1,'delivery_date':1, 'date': 1, 'status':1, 'order_total':1}}
=======
    {'$project': {'item_info._id': 1, 'item_info.Type':1,'item_info.Category':1,'item_info.Color':1,'item_info.Seller':1,'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1, 'item_details.status':1,'item_details.price': 1,  'item_details.quantity': 1, 'status':1,'item_details.size':1,'delivery_date':1, 'date': 1, 'order_info.order_total':1}}
>>>>>>> upstream/master
])
    return render_template('orders.html',title='My Orders',dict_order_details=dict_order_details)

@users.route('/my_orders/cancel_order<string:order_id>')
@login_required
def cancel_order(order_id):
    id=current_user.get_id()
    user_order_count=mongo.db.order.find({'_id':ObjectId(order_id)}).count()
    if user_order_count:
        user_order=mongo.db.order.find_one({'_id':ObjectId(order_id)})
        items=user_order['item_details']
        for item in items:
            item_size='Size.'+item['size']
            mongo.db.items.update_one({'_id':item['item_id']},
                {'$inc':
                    {
                    item_size:item['quantity']
                    }
                }
                )
        mongo.db.order.delete_one({'_id':ObjectId(order_id)})
    return redirect(url_for('users.orders'))

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

'''
@users.route('/user/address/update')
@login_required
def update_address(address):
    id = current_user.get_id()
    form=DeliveryForm()
    if form.validate_on_submit():
        address={
            'name':form.name.data,
            'address':form.address.data,
            'state':form.state.data,
            'city':form.city.data,
            'pin_code':form.pin_code.data,
                   }
        mongo.db.user.update_one({'_id':ObjectId(id)},
            {
            '$set':
            {
            'list_address.n':address
            }
            })
        flash('Your address has been updated','success')
        return redirect(url_for('users.checkout'))
    elif request.method=='GET':

    return redirect(url_for('users.address'))
'''

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
<<<<<<< HEAD
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.objects(email=form.email.data).first()
            if user is None:
                flash('There is no account with this email.', 'danger')
                return redirect(url_for('users.reset_request'))
=======
    #print('fkbvjkbrvkbrkv brkv')
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        print('jjjjj')
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.objects(email=form.email.data).first()
            print('ggggggggggg')
            if user is None:
                flash('There is no account with this email.', 'danger')
                return redirect(url_for('users.reset_request'))
            print('hhhhhhhhhhhhhhhhhh')
>>>>>>> upstream/master
            send_reset_email(user)
            flash('An email has been sent with instructions to rest your password', 'success')
            return redirect(url_for('users.login'))
        return render_template('reset_request.html', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
<<<<<<< HEAD
    if current_user.is_authenticated():
=======
    if current_user.is_authenticated:
>>>>>>> upstream/master
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is an invalid or expired token', 'danger')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
<<<<<<< HEAD
        hashpass = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
        db.session.commit()
        flash('Your password has benn updated!', 'success')
        redirect(url_for('login'))
=======
        print(form.password.data)
        hashpass = generate_password_hash(form.password.data,method='sha256')
        mongo.db.user.update({'_id':ObjectId(current_user.get_id())
            },
            {
            '$set':
            {
                'password':hashpass
            }
            }
            )
        flash('Your password has benn updated!', 'success')
        return redirect(url_for('users.login'))
>>>>>>> upstream/master

    return render_template('reset_token.html', form=form)


@users.route('/review/<string:item_id>', methods=['GET', 'POST'])
@login_required
def review(item_id):
    user_already_reviewed=mongo.db.review.find({'item_id':ObjectId(item_id),'reviews.user_id':current_user.get_id()}).count()
    if user_already_reviewed:
        flash('You have aready reviewed on this item','success')
        return redirect(url_for('users.update_review',item_id=item_id))
    form=ReviewForm()
    if form.validate_on_submit():
        name_dict=mongo.db.user.find_one({'_id':ObjectId(current_user.get_id())},{'_id':0,'username':1})
        name=name_dict['username']
        review={
        'user_id':current_user.get_id(),
        'user_name':name,
        'date':datetime.now(),
        'rating':form.rating.data,
        'headline':form.headline.data,
        'review':form.review.data
        }
        print(review)
        count=mongo.db.review.find({'item_id':ObjectId(item_id)}).count()
        if count:
            mongo.db.review.update_one({'item_id':ObjectId(item_id)},
                        {
                        '$push':{
                            'reviews':review
                        }
                        })
        else:
            mongo.db.review.insert_one({'item_id':ObjectId(item_id),'reviews':[review]})
        flash('Your review has been submitted','success')
        return redirect(url_for('main.item',item_id=item_id))
    item=mongo.db.items.find_one({'_id':ObjectId(item_id)})
    return render_template('review.html', title='Review',Legend='Create Review', form=form,item=item)

@users.route('/review/delete/<string:item_id>')
@login_required
def delete_review(item_id):
    user_already_reviewed=mongo.db.review.find({'item_id':ObjectId(item_id),'reviews.user_id':current_user.get_id()}).count()
    if user_already_reviewed==0:
        flash("You don't have permissions to delete this review","danger")
        return redirect(url_for('main.item', item_id=item_id))
    else:
        mongo.db.review.update_one({'item_id':ObjectId(item_id)},
                {
                    '$pull':
                        {
                            'reviews':
                            {
                            'user_id':current_user.get_id()
                            }
                        }

                })
        flash('Your review has been deleted','success')
        return redirect(url_for('main.item',item_id=item_id))


@users.route('/review/update/<string:item_id>', methods=['GET', 'POST'])
@login_required
def update_review(item_id):
    user_already_reviewed=mongo.db.review.find({'item_id':ObjectId(item_id),'reviews.user_id':current_user.get_id()}).count()
    if user_already_reviewed==0:
        flash("You don't have permissions to delete this review","danger")
        return redirect(url_for('main.item', item_id=item_id))
    else:
        form=ReviewForm()
        if form.validate_on_submit():
            mongo.db.review.update_one({'item_id':ObjectId(item_id), 'reviews.user_id':current_user.get_id()},
                    {
                        '$set':
                        {
                            'reviews.$.rating':form.rating.data,
                            'reviews.$.date':datetime.now(),
                            'reviews.$.headline':form.headline.data,
                            'reviews.$.review':form.review.data
                        }
                    })
            flash('Your review has been upated!', 'success')
            return(redirect(url_for('main.item',item_id=item_id)))
        elif request.method=='GET':
            user_reviews = mongo.db.review.aggregate([
                                {'$unwind': '$reviews'},
                                {'$match': {'item_id': ObjectId(item_id), 'reviews.user_id': current_user.get_id()}},
                                {'$project': {'_id': 0, 'name':'$reviews.user_name','date':'$reviews.date','rating':'$reviews.rating', 'headline':'$reviews.headline', 'review':'$reviews.review'}}
                            ])
            for user_review in user_reviews:
                form.rating.data=user_review['rating']
                form.headline.data=user_review['headline']
                form.review.data=user_review['review']
            item=mongo.db.items.find_one({'_id':ObjectId(item_id)})
        return render_template('review.html',title='Update Review',Legend='Update Review',item=item, form=form)

