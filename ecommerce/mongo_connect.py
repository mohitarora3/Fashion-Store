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
# hashpass = generate_password_hash('password', method='sha256')
# mongo.db.user.insert_one({'username':'Mohit Arora','email':'arora3mohit@gmail.com', 'password':hashpass, 'role':'adminmo
'''
mongo.db.items.create_index([
    ('Category': 'text'),
    ('Type': 'text'),
    ('Brand': 'text'),
    ('Short Description': 'text'),
    ('Description': 'text')
],
    {
        'weights': {
            'Category': 10,
            'Type': 8,
            'Description': 5,
            'Brand': 3
        },
        'name': "TextIndex"
}
)
{"Category":"text",
 "Type": "text",
 "Brand":"text",
 "Short Description": "text",
 "Description" :"text"
}
'''
for a in mongo.db.items.find(
        {"$text": {"$search": "red color shirt for women"}}):
  print(a)
