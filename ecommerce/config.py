import os


class Config:
    SECRET_KEY = '1230ab'
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    #MONGO_URI = 'mongodb://vidulkumar:New2mlab@ds157493.mlab.com:57493/mydatabase'
    MONGO_URI = "mongodb://localhost:27017/mydatabase"
    