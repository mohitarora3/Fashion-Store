import os


class Config:
    SECRET_KEY = '1230ab'
    Mail_SERVER = 'smtp.googleemail.com'
    Mail_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MONGO_URI = "mongodb://localhost:27017/myDatabase"
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = 'public'
    RECAPTCHA_PRIVATE_KEY = 'ppublic'
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    RECAPTCHA_SITE_KEY = '6LdJ4GcUAAAAAN0hnsIFLyzzJ6MWaWb7WaEZ1wKi'
    RECAPTCHA_SECRET_KEY = '1230ab'
