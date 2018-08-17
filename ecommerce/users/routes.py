from flask import render_template, redirect, url_for, Blueprint, flash
from flask_login import current_user, login_required, login_user, logout_user
from ecommerce.users.forms import RequestResetForm, ResetPasswordForm, RegistrationForm, LoginForm
from ecommerce import db
from ecommerce.models import User

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='register', form=form)


@users.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return render_template(url_for('main.home'))


@users.route('/saving/<string:item_id>')
@login_required
def add_to_cart():
    current_user.cart = item_id
    db.session.commit()
    return render_template('home.html')


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
