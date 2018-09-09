from flask import Flask
from flask_pymongo import PyMongo
from jsonmerge import merge
from bson.objectid import ObjectId
import pprint
from flask import request
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"


mongo = PyMongo(app)

# mongo.db.items.update({"Brand": "Highlander"}, {"$set": {"Quantity": 10}})
# mongo.db.items.update({"Brand":"Campus Sutra"}, {"$set": {"Quantity": 10}})
# mongo.db.items.update({"Brand":"Hire&Now"}, {"$set": {"Quantity": 10}})
# mongo.db.items.update({"Brand":"Nautica"}, {"$set": {"Quantity": 10}})
'''
item = mongo.db.user.find_one({'_id': ObjectId('5b92b765eaeeee16b8589a32'), 'item.item_id': '5b92aa02eaeeee126482fcdd', 'item.size': '42'})
print(item)
for i in mongo.db.user.find():
print(i)

'''

'''

for x in mongo.db.items.find():
d = x["Size"]
for key, val in d.items():
    if(val > 0):
        print(key)
a = mongo.db.items.update({"Brand": "Highlander"}, {"$set": {"Size.42": 5}})

a = mongo.db.items.find()
for i in mongo.db.items.find():
print(i)
# mongo.db.items.delete_many({})
# mongo.db.user.update({'_id': ObjectId('5b92b765eaeeee16b8589a32')}, {'$push': 'item':{'item_id': '5b92aa02eaeeee126482fcdd' }{'quantity': 1}})
# for item_already_present:
# for i in item['item']:
#   print(i)



for i in mongo.db.user.find():
print(i)
bag_mrp = 0
bag_price = 0
lst = []
dict = {}
Items = mongo.db.user.find_one(
{"_id": ObjectId('5b94c0faeaeeee02689ecb67')
 },
{
    "_id": 0, "item": 1
}
)
Items = Items['item']
print(Items)
for item in Items:
id = item['item_id']
size = item['size']
print(id)

for a in mongo.db.items.find({'_id': ObjectId(id)}):
    a['quantity'] = 1
    a['size'] = size
    print(a['Mrp'])
    bag_mrp = bag_mrp + a['Mrp']
    bag_price += a['Price']
    print('rfmrmltrmk')
    lst.append(a)
dict['bag_discount'] = bag_mrp - bag_price
dict['bag_mrp'] = bag_mrp
dict['bag_total'] = bag_price
print(lst)
print(dict)



mongo.db.user.update_one(
{"_id": ObjectId('5b94c0faeaeeee02689ecb67'), "item.item_id": '5b94e49ceaeeee1b1cad4b39'
},
{"$set": {"item.$.quantity": 100}
}
)


# mongo.db.user.update({'_id': ObjectId('5b94c0faeaeeee02689ecb67'), "item.item_id": ObjectId('5b94e49ceaeeee1b1cad4b3b')}, {'$pull': {"item.$.item_id": ObjectId('5b94e49ceaeeee1b1cad4b3b')}})



mongo.db.user.update_one(
{"_id": ObjectId('5b94c0faeaeeee02689ecb67')
},
{"$unset":
{"item": 1
}
}
'''


def add():
    '''mongo.db.user.update_one({"_id": ObjectId('5b955a39eaeeee2c588a716a')},
                             {"$pull": {"item": {"item_id": '5b94e49ceaeeee1b1cad4b39'}}})


    mongo.db.user.update_one(
        {"_id": ObjectId(id),
         "item.item_id": item_id,
         "item.size": item_size
         },
        {"$set":
         {"item.$.quantity": 4}
         }
    )
    '''
    item = mongo.db.user.find_one({"$and": {'item.item_id': '5b94e49ceaeeee1b1cad4b39'}, {'item.size': '44'}})
    print(item)
    if item is None:
        print('rnkn')
        a = {"item_id": item_id, "size": 44, "quantity": 1}
        mongo.db.user.update_one(
            {"_id": ObjectId('5b94e49ceaeeee1b1cad4b39')
             },
            {"$push":
             {"item": a
              }
             }
        )

    for i in mongo.db.user.find():
        print(i)


if __name__ == '__main__':
    add()
