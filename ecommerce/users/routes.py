from flask import render_template, redirect, url_for, Blueprint, flash, request
from flask_login import current_user, login_required, login_user, logout_user
from ecommerce.users.forms import RequestResetForm, ResetPasswordForm, RegistrationForm, LoginForm
from ecommerce import db, bcrypt, mongo
from ecommerce.models import User
from bson.objectid import ObjectId

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        users = mongo.db.customers
        users.insert({"username": form.username.data, "email": form.email.data, "password": hashed_password})
        flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        users = mongo.db.customers
<<<<<<< HEAD
        login_user = users.find_one({'email': request.form['email']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['email'] = request.form['email']
                flash('You have been successfully logged in', 'success')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
=======
        user = users.find({"email": form.email.data})
        p = user["password"]
        if user and bcrypt.check_password_hash(p, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
>>>>>>> 0f0c6b1604d91563c852b7e4cc7e8e36b5b0d382
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return render_template(url_for('main.home'))


@users.route('/saving/<string:item_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(item_id):
    id = "1234"
    users = mongo.db.customers
    # users.update({"_id": ObjectId(id)}, {$set: {cart_item_ids: item_id}})
    flash('This item has been successfully added to cart', 'success')
    return render_template('home.html')


@users.route('/removing/<string:item_id>')
@login_required
<<<<<<< HEAD
def remove_from_cart(item_id):
    id = current_user.get_id()
    users = mongo.db.customers
    # users.update({"_id": ObjectId(id)}, {$pull: {"cart_item_ids": item_id}})
=======
def add_to_cart():
    id = current_user.get_id()
    users = mongo.db.customers
    users.update({"_id": ObjectId(id)}, {$push: {"cart_item_ids": item_id}})
    flash('This item has been successfully added to cart', 'success')
    return render_template('home.html')


@users.route('/removing/<string:item_id>')
@login_required
def remove_from_cart():
    id = current_user.get_id()
    users = mongo.db.customers
    users.update({"_id": ObjectId(id)}, {$pull: {"cart_item_ids": item_id}})
>>>>>>> 0f0c6b1604d91563c852b7e4cc7e8e36b5b0d382
    flash('Successfully Removed', 'success')
    return render_template('home.html')


<<<<<<< HEAD
@users.route('/ my_cart', methods=['GET', 'POST'])
=======
@users.route('/ my_cart / )
>>>>>>> 0f0c6b1604d91563c852b7e4cc7e8e36b5b0d382
@login_required
def cart():
    id = current_user.get_id()
    users = mongo.db.customers.find({"_id": ObjectId(id)})
    item = users["cart_item_ids"]
    return render_template('cart.html', users=users, item=items)


@users.route('/reset_password')
def reset_request():
    if current_user.is_authenticated():
        return redirect(url_for('main.home'))
    else:
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                flash('There is no account with this email.', 'danger')
                return redirect(url_for('reset_request'))
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
        user.password = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
        db.session.commit()
        flash('Your password has benn updated!', 'success')
        redirect(url_for('login'))

    return render_template('reset_token.html', form=form)
