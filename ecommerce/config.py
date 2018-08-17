import os

class Config:
	SECRET_KEY='1230ab'	
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	Mail_SERVER='smtp.googleemail.com'
	Mail_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
	MONGO_URI="mongodb://localhost:27017/myDatabase"