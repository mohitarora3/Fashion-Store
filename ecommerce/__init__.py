from flask import Flask
from ecommerce.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager
from flask_pymongo import PyMongo

mongo=PyMongo()
mail = Mail()
db = SQLAlchemy()
bcrypt= Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
def create_app(config_class=Config):
	app=Flask(__name__)
	app.config.from_object(Config)

	mongo.init_app(app)
	mail.init_app(app)
	bcrypt.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	from ecommerce.main.routes import main
	from ecommerce.users.routes import users

	app.register_blueprint(main)
	app.register_blueprint(users)

	return app