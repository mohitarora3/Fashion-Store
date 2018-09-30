from flask import Flask
from flask_pymongo import PyMongo
from jsonmerge import merge
from bson.objectid import ObjectId
from users.forms import DeliveryForm
import pprint
from flask import request
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"


mongo = PyMongo(app)


number = '0'
a = 'list_address.' + number
'''
mongo.db.user.update_one({"_id": ObjectId('5b955a39eaeeee2c588a716a')
                          },
                         {"$unset":
                          {a: 1}
                          }
                         )

'''
mongo.db.user.update_one({"_id": ObjectId('5b955a39eaeeee2c588a716a'), "list_address": ""},
                         {"$pull":
                          {"list_address.$": None
                           }
                          }

                         )


for i in mongo.db.user.find():
  print(i)

'''
if address>0:
  address=mongo.db.user.find({'_id':ObjectId('5b9d51f2eaeeee281c933160')

a = address['list_address']
for i in a:
  print(i)



form4 = DeliveryForm([('name', 'jerry'), ('address', 'jerry@mail.com'), ('city', "Delhi"), ('state', 'Delhi'), ('pin_code', '110033')])


mongo.db.user.update_one({'_id': ObjectId('5b955a39eaeeee2c588a716a')},
                         {'$unset':
                          {'list_address': 1}
                          }
                         )
'''
