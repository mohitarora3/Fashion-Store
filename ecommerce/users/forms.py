from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ecommerce.models import User
from flask_login import current_user
from ecommerce import mongo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        users = mongo.db.customers
        user = users.find_one({'username': username.data})
        if user:
            raise ValidationError('That username is alreay taken. Please choose a different one')

    def validate_email(self, email):
        users = mongo.db.customers
        user = users.find_one({'email': email.data})
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class DeliveryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=15)])
    address = TextAreaField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    pin_code = IntegerField('Pin Code', validators=[DataRequired()])
    phone_number = StringField('Mobile Number', validators=[DataRequired(), Length(10)])
    submit = SubmitField('Save')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Request Reset Password')

    def validate_email(self, email):
        users = mongo.db.customers
        user = users.find({'email': email.data})
        if user is None:
            raise ValidationError('There is no account with that email. You must register first')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('Reset Password')


class UpdateAccountForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is alreay taken. Please choose a different one.')

    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This email is alreay taken. Please choose a different one.')
