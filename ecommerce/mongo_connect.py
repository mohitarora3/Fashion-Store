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
app.config['MONGO_URI'] = "mongodb://vidulkumar:New2mlab@ds157493.mlab.com:57493/mydatabase"
# app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"
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
while(i < len(brands)):
  price.append(brands[i])
  i = i + n
print(price)
'''
id = '5be6b480eaeeee29e026fd1b'
'''
mongo.db.user.update_one(
    {"_id": ObjectId(id),
     "item.item_id": ObjectId('5be5d455eaeeee0ef45458a0'),
     "item.size": 'Double King'
     },
    {"$set":
     {"item.$.quantity": 5}
     }
)




id = '5be7e2e515ac88187069d191'
# cart_status = mongo.db.user.find({'$and': [{'$match':{'_id': ObjectId(id)}, {'wishlist': {'$exists': 'true'}}]}).count()

result = mongo.db.user.aggregate([{'$match': {'_id': ObjectId("5be6b480eaeeee29e026fd1b")}},
                                  {'$project':
                                   {'_id': 0, 'wishlist': 1, 'count':
                                    {'$size': '$wishlist'}
                                    }
                                   }
                                  ])
items_dict = mongo.db.user.aggregate([
    {'$match': {'_id': ObjectId("5be6b480eaeeee29e026fd1b")}},
    {'$lookup':
     {
         'from': 'items',
         'localField': 'wishlist.item_id',
         'foreignField': '_id',
         'as': 'item_info'
     }
     },
    {'$project': {'_id': 0, 'item_info.Category': 1, 'item_info._id': 1, 'item_info.Type': 1, 'item_info.Category': 1, 'item_info.Color': 1, 'item_info.Seller': 1, 'item_info.Image': 1, 'item_info.Brand': 1, 'item_info.Short Description': 1},
     }
])
'''
mongo.db.items.insert_many([{
      "Image": ['46.1.jpg', '46.2.jpg', '46.3.jpg', '46.4.jpg'],
      "Brand": "Roadster",
      "Type":"Casual Shirt",
      "Category":"Men",
      "Seller":"WandWagon",
      "Short Description": "Charcoal printed casual shirt",
      "Description": "Charcoal printed casual shirt, has a mandarin collar collar, button placket, long sleeves, curved hem",
      "Mrp": 1199,
      "Discount": 0,
      "Price": 1199,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this top-of-the-line shirt by Roadster. This blue piece can be worn with dark wash jeans and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['47.1.jpg', '47.2.jpg', '47.3.jpg', '47.4.jpg'],
      "Brand": "Roadster",
      "Type":"Casual Shirt",
      "Category":"Men",
      "Seller":"WandWagon",
      "Short Description": "Men Blue Denim Washed Casual Shirt",
      "Description": "Blue washed denim casual shirt, has a mandarin collar, a full button placket, long sleeves, curved hem",
      "Mrp": 1499,
      "Discount": 30,
      "Price": 1049,
      "Size": {'38': 0, '40': 25, '42': 10, '44': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this top-of-the-line shirt by Roadster. This blue piece can be worn with dark wash jeans and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['48.1.jpg', '48.2.jpg', '48.3.jpg', '48.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Prologue",
      "Short Description": "Men's Blue 1969 Slim Jeans",
      "Description": "Blue washed Men's Blue 1969 Slim Jeans",
      "Mrp": 1969,
      "Discount": 20,
      "Price": 1576,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['49.1.jpg', '49.2.jpg', '49.3.jpg', '49.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Proleague",
      "Short Description": "Men's Blue Jeans in Athletic Fit with GapFlex",
      "Description": "Blue washed Men's Blue Jeans in Athletic Fit with GapFlex",
      "Mrp": 3999,
      "Discount": 20,
      "Price": 3200,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['50.1.jpg', '50.2.jpg', '50.3.jpg', '50.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Proleague",
      "Short Description": "Men's Blue Jeans in Slim Fit",
      "Description": "Blue washed Men's Blue Jeans in Slim Fit",
      "Mrp": 4999,
      "Discount": 20,
      "Price": 4000,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['51.1.jpg', '51.2.jpg', '51.3.jpg', '51.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Proleague",
      "Short Description": "Men's Grey Soft Wear Jeans In Slim Fit With GAPFLEX",
      "Description": "Grey washed Men's Grey Soft Wear Jeans In Slim Fit With GAPFLEX",
      "Mrp": 3999,
      "Discount": 20,
      "Price": 3200,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['100% Cotton', 'Machine-wash'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['52.1.jpg', '52.2.jpg', '52.3.jpg', '52.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Proleague",
      "Short Description": "Olive Green Slim Fit Cords",
      "Description": "Men's Olive Green Slim Fit Cords With Gapflex",
      "Mrp": 3799,
      "Discount": 20,
      "Price": 3040,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['98% cotton', '2% spandex'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['53.1.jpg', '53.2.jpg', '53.3.jpg', '53.4.jpg'],
      "Brand": "GAP",
      "Type":"Jeans",
      "Category":"Men",
      "Seller":"Proleague",
      "Short Description": "Blue Skinny Fit Stretchable Jeans",
      "Description": "Men Blue Skinny Fit Mid-Rise Low Distress Stretchable Jeans",
      "Mrp": 1499,
      "Discount": 10,
      "Price": 1349,
      "Size": {'30': 0, '32': 25, '34': 10, '38': 6},
      "Product Details": "GAP is one of the world's most iconic apparel and accessories brands and the authority on American casual style. Today, GAP continues to be the best destination for wardrobe essentials such as denim, tees, hoodies and great-fitting pants.",
      "Material & Care": ['98% cotton', '2% elastane', 'Machine Wash'],
      "Complete The Look": "Keep warm on the coldest of days with this dark wash jeans by Proleague. This blue piece can be worn with top-of-the-line shirt and Chelsea boots when youre going to an after-work happy hour."
  },
  {
      "Image": ['40.1.jpg', '40.2.jpg', '40.3.jpg', '40.4.jpg'],
      "Brand": "LOCOMOTIVE",
      "Type":"Leather Jacket",
      "Category":"Men",
      "Seller":"Wiztech Crop",
      "Short Description": "Men Leather Jacket",
      "Description": "Men Black Solid Leather Jacket",
      "Mrp": 4449,
      "Discount": 60,
      "Price": 1779,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black solid leather jacket, has a mock collar, two pockets, zip closure, long sleeves, straight hem, faux fur lining",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  },
  {
      "Image": ['41.1.jpg', '41.2.jpg', '41.3.jpg', '41.4.jpg'],
      "Brand": "Mast&Harbour",
      "Type":"Leather Jacket",
      "Category":"Men",
      "Seller":"RealTech Ltd.",
      "Short Description": "Men Black Solid Jacket",
      "Description": "Men Black Solid Bomber Jacket",
      "Mrp": 4299,
      "Discount": 40,
      "Price": 2579,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black solid bomber, has a stand collar, four pockets, zip closure, long sleeves, straight hem, polyester lining",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }, {
      "Image": ['42.1.jpg', '42.2.jpg', '42.3.jpg', '42.4.jpg'],
      "Brand": "Sera",
      "Type":"Skirt",
      "Category":"Women",
      "Seller":"FashionTech",
      "Short Description": "Women Flared Skir",
      "Description": "Women Black & Off-White Printed Flared Skir",
      "Mrp": 1294,
      "Discount": 40,
      "Price": 776,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black, off-white and peach-coloured printed flared skirt, has zip closure, attached lining",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }, {
      "Image": ['43.1.jpg', '43.2.jpg', '43.3.jpg', '43.4.jpg'],
      "Brand": "Martini",
      "Type":"Skirt",
      "Category":"Women",
      "Seller":"Elixirnet",
      "Short Description": "Women Black Flared Skirt",
      "Description": "Women Black Solid Flared Skirt",
      "Mrp": 999,
      "Discount": 30,
      "Price": 699,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black solid flared knee-length skirt, has a waistband with a concealed zip closure, a flared hem",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }, {
      "Image": ['44.1.jpg', '44.2.jpg', '44.3.jpg', '44.4.jpg'],
      "Brand": "SASSAFRAS",
      "Type":"Jacket",
      "Category":"Women",
      "Seller":"Elixirnet",
      "Short Description": "Women Black & Yellow Floral Casual Blazer",
      "Description": "Women Black & Yellow Floral Print Single-Breasted Casual Blazer",
      "Mrp": 2199,
      "Discount": 40,
      "Price": 1319,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Black, yellow and olive green floral print casual blazer, has a peaked lapel, single-breasted with a button closure, long sleeves, two flap pockets, a straight hem, and an attached lining",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }, {
      "Image": ['45.1.jpg', '45.2.jpg', '45.3.jpg', '45.4.jpg'],
      "Brand": "Zima Leto",
      "Type":"Jacket",
      "Category":"Women",
      "Seller":"Proleague",
      "Short Description": "Women Blue Embroidered Tailored Fit Casual Blazer",
      "Description": "Women Blue Embroidered Front Open Tailored Fit Casual Blazer",
      "Mrp": 2249,
      "Discount": 30,
      "Price": 1574,
      "Size": {'S': 0, 'M': 25, 'L': 10, 'XL': 6},
      "Product Details": "Blue embroidered front open casual blazer, has a mandarin collar, long sleeves, and an attached lining",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  }
 ])
'''
for items in items_dict:
  for item in items['item_info']:
    # i = i['item_info']
    print(item['Brand'])
'''
