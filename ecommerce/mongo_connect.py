import bcrypt
from flask import Flask
from flask_pymongo import PyMongo
# from jsonmerge import merge
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# from models import user
from werkzeug.security import generate_password_hash
# from users.forms import DeliveryForm
import pprint
import math
from flask import request
import json
from bson.json_util import dumps

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://vidulkumar:New2mlab@ds157493.mlab.com:57493/mydatabase"
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
# hashpass = generate_password_hash('password', method='sha256')
# mongo.db.user.insert_one({'username':'Mohit Arora','email':'arora3mohit@gmail.com', 'password':hashpass, 'role':'adminmo


#      Admin details and commands to insert document in user collection
'''
hashpass = generate_password_hash("mohitarora123", method='sha256')
mongo.db.user.insert_one(
      {
      "username":"Mohit Arora",
      "email":"arora3mohit@gmail.com",
      "password":hashpass,
      "role":"admin"
      }
      )


id="5c6d39ac4ec651035420c742"
hashpass = generate_password_hash('6666')
print(hashpass)
mongo.db.user.update({'_id':ObjectId(id)
            },
            {
            '$set':
            {
                'password':hashpass
            }
            }
            )

data={
      'Brand':['Higlander','Campus Sutra'],
      'Discount':10,
      'Category':['Men','Women']
      };
search= mongo.db.items.find(
            {'$and':[
           {"$or":[ {'Brand':'Highlander'},{"Brand":"Campus Sutra"},{'Brand':'Harpa'}]},
           {'Discount':{'$gt':10}},
           {"$or":[{"Category":"Men"},{"Category":"Women"}]}
           ]}
           )

# search={}
ans={'Brand':[]}
     # search['Brand']={'$or':{Brand:"

if len(data['Brand'])>1:
       for brand in data['Brand']:
             ans['Brand']+="{Brand:"+brand+"},"
print(ans)

# for i in search:
#       print(i['Brand'],i['Discount'],i['Category'])
'''
brands = mongo.db.items.distinct('Brand', {'Category': "Women", "Type": 'Shirt'})
for i in brands:
  print(i)
