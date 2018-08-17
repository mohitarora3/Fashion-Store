from flask_mail import Message
from  ecommerce import mail

def send_reset_email(user):
	token = user.get_reset_token()
	msg= Message('Password Reset Request',
			sender= 'noreply@demo.com',
			recipents=[user.email] )
	msg.body= '''To reset your password, visit the following link {}
			If you did not make this request then simply ignore this email and no changes will be made.
			'''.format(url_for('users.reset_token',token='token'))
	
	mail.send(msg)			