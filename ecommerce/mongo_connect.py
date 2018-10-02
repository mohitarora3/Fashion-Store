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
                          {'list_address': 1}
                          }
                         )


mongo.db.user.update_one({"_id": ObjectId('5b955a39eaeeee2c588a716a'), "list_address": ""},
                         {"$pull":
                          {"list_address.$": None
                           }
                          }

                         )



dict_items_info = mongo.db.user.find_one({'_id': ObjectId('5b955a39eaeeee2c588a716a')}, {'_id': 0, 'item': 1, 'list_address': 1})

lst_items_info = dict_items_info['item']
for item_info in lst_items_info:
  item_size = 'Size.' + item_info['size']
  mongo.db.items.update_one({'_id': ObjectId(item_info['item_id'])},
                            {'$inc':
                             {item_size: -item_info['quantity']
                              }
                             }
                            )

a = dict_items_info['list_address']
print(a[2])

'''
for i in mongo.db.items.find():
  print(i)
for i in mongo.db.order.find():
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
