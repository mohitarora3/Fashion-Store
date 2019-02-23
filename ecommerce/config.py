import os


class Config:
    SECRET_KEY = '1230ab'
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    #MAIL_USERNAME = 'arora3mohit@gmail.com'
    #os.environ.get('MAIL_USERNAME')
    #os.environ.get('MAIL_PASSWORD')
    SOCIAL_FACEBOOK = {
    'consumer_key': '2246910702234554',
    'consumer_secret': '1724128f42762d9897832bc39cdcd5cf'
    }
   #MONGO_URI = 'mongodb://vidulkumar:New2mlab@ds157493.mlab.com:57493/mydatabase'
    MONGO_URI = "mongodb://localhost:27017/mydatabase"
    