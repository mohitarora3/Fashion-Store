from flask import Flask
from flask_pymongo import PyMongo
from jsonmerge import merge
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# from users.forms import DeliveryForm
import pprint
import math
from flask import request
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://vidulkumar:New2mlab@ds157493.mlab.com:57493/mydatabase"
# app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
hashpass = generate_password_hash('password', method='sha256')
mongo.db.user.insert_one({'username':'Mohit Arora','email':'arora3mohit@gmail.com', 'password':hashpass, 'role':'admin'})
print('elnf')

