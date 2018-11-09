from flask import Flask
from flask_pymongo import PyMongo
from jsonmerge import merge
from bson.objectid import ObjectId
# from users.forms import DeliveryForm
import pprint
import math
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
                          {'item': 1}
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
# for i in mongo.db.items.find():
# print(i)
# mongo.db.order.delete_many({})

'''

a = mongo.db.order.aggregate([
    {'$match': {'user_id': '5bb5f391eaeeee21f4c15bba'}},
    #{'$unwind': '$item_details'},
    {'$lookup':
     {
         'from': 'items',
         'localField': 'item_details.item_id',
         'foreignField': '_id',
         'as': 'item_info'
     }
     },
    {'$project': {'item_info._id': 1, 'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1, 'item_details.mrp': 1, 'item_details.discount': 1, 'item_details.quantity': 1, 'date': 1, 'delivery_details': 1}}
    #{'$unwind': '$item_info'}




])

for i in a:
    print(i)

        n = len(i['item_details'])
    for j in range(n):
        i['item_details'][j] = {**i['item_details'][j], **i['item_info'][j]}
        # print(i)

# mongo.db.order.delete_many({})
from datetime import datetime
a = datetime.now().date()
# mongo.db.user.update_one({}, {'$unset': {'item': 1}})
for i in mongo.db.items.find():
  print(i)
  item = mongo.db.user.find({'_id': ObjectId('5b955a39eaeeee2c588a716a'), 'item.item_id': item_id, 'item.size': request.form['si']}).count()

dict_order_details = mongo.db.order.aggregate([
    {'$match': {'user_id': '5bb5f391eaeeee21f4c15bba'}},
    {'$lookup':
     {
         'from': 'items',
         'localField': 'item_details.item_id',
         'foreignField': '_id',
         'as': 'item_info'
     }
     },
    {'$project': {'item_info._id': 1, 'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1, 'item_details.price': 1, 'item_details.quantity': 1, 'item_details.size': 1, 'delivery_date': 1, 'date': 1, 'status': 1, 'order_total': 1}
     }

])

for i in mongo.db.items.find({}):
  item_image = i["Image"]
  for image in item_image:
    print(image)
'''
# mongo.db.review.delete_many({})
'''
review = {
    'user_id': 'f;mtlt',
    'rating': 5,
    'headline': 'awesome',
    'review': 'best'
}
count = mongo.db.review.find({'item_id': ObjectId('5b94e49ceaeeee1b1cad4b3c')}).count()
if count:
  print(count)
  mongo.db.review.update_one({'item_id': ObjectId('5b94e49ceaeeee1b1cad4b3c')},
                             {
      '$push': {
          'reviews': review
      }
  })
else:
  mongo.db.review.insert_one({'item_id': ObjectId('5b94e49ceaeeee1b1cad4b3c'), 'reviews': [review]})

mongo.db.review.delete_many({})

for i in mongo.db.user.find():
  print(i)
ans = mongo.db.user.find_one({'_id': ObjectId('5bb5f391eaeeee21f4c15bba')},
                             {
    '_id': 0, 'list_address': 1
})
print(ans)

review = {
    'rating': 5,
    'headline': 'Good',
    'review': 'Size fit is nice'
}
mongo.db.review.update_one({'item_id': ObjectId('5b94e49ceaeeee1b1cad4b3c'), 'reviews.user_id': '5bb5f391eaeeee21f4c15bba'},
                           {
    '$set':
    {
        'reviews.$.rating': 5,
    'reviews.$.headline': 'Good',
    'reviews.$.review': 'Size fit is nice'
    }
})


review = mongo.db.review.find_one({'item_id': ObjectId('5b94e49ceaeeee1b1cad4b3c'), 'reviews.user_id': '5bb5f391eaeeee21f4c15bba'}, {'reviews.$': 1, '_id': 0})
print(review)

review = mongo.db.review.aggregate([
    {'$unwind': '$reviews'},
    {'$match': {'item_id': ObjectId('5b94e49ceaeeee1b1cad4b39'), 'reviews.user_id': '5b955a39eaeeee2c588a716a'}},
    {'$project': {'_id': 0, 'name': '$reviews.user_name', 'rating': '$reviews.rating', 'headline': '$reviews.headline', 'review': '$reviews.review'}}
])
for i in review:b
  print(i)

for i in mongo.db.user.find():
  print(i)

mongo.db.items.createIndex({'Brand': 'text', 'Short Description': 'text', 'Description': 'text'})
a = mongo.db.items.find({'$text': {'$search': 'highlander'}})
for i in a:
  print(i)

# mongo.db.review.delete_many({})
review = mongo.db.review.aggregate([{'$project':
                                     {
                                         'rating_avg': {'$avg': '$reviews.rating'},
                                         'number': {'$size': '$reviews'},
                                         'reviews': '$reviews'
                                     }}])
for i in review:
  for
  print(i)


# mongo.db.items.update({}, {'$set': {'Type': 'Shirt', 'Category': 'Men'}}, {'$multi': 'true'})
for i in mongo.db.items.find({}):
  print(i)
# mongo.db.items.create_index([('Brand': 'text')])
# results = mongo.db.command('text', 'items', search='Campus')

print("rsults")
search_results = mongo.db.items.find({'$text': {'$search': "\"highlander white\""}})
for i in search_results:
  print(i)

item = mongo.db.items.find_one({"_id": ObjectId('5be1a25deaeeee255c987c5c')})
similar_products = mongo.db.items.find({'Category': item['Category'], 'Type': item['Type'], '_id': {'$not': item['_id']}}).limit(3)
for item in similar_products:
  print(item)

brands = mongo.db.items.distinct('Price', {'Type': 'Bedsheet'})
brands.sort()
print(brands)
n = math.ceil(len(brands) / 3)
print(n)
i = 0
price = []
While(i < len(brands)):
  price.append(brands[i])
  i = i + n
print(price)
'''


mongo.db.user.delete_many({})
for i mongo.db.users.find():
  print(i)
