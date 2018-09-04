from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import pprint

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"


mongo = PyMongo(app)


def add():
    '''
    mongo.db.user.update_one(
        {"_id": ObjectId("5b7ef8f3ba58e927aebafb72")
         },
        {"$push": {
            "cart_item_ids": item_id
        }
        }
    )

    a = mongo.db.user.find_one({'email': 'mohit5@gmail.com'})
    print(a)
    mongo.db.user.update(
        {'email': 'mohit5@gmail.com'},
        {'$unset':
         {'item': ''}
         }

    )
    '''

    Items = mongo.db.user.find_one({'email': 'mohit5@gmail.com'}, {'_id': 0, 'item': 1})
    # print(Items)
    Items = Items['item']
    # print(Items)
    dict = {}
    for item in Items:
        # print(item)
        id = item[0]['item_id']
        i = mongo.db.items.find_one({'_id': ObjectId(id)})
        i['Size'] = item[1]['size']
        # dict.add(i)
        print(i)
    #for item in Items:
        #print(item)
    '''    items = mongo.db.items
    a = items.estimated_document_count()
    documents = items.find()
    d = items.find_one({"Brand": "Highlander"})
    arr = d["Size"]
    print(arr)
    print(d["Size"][3])
    for i in arr:
        print(i)
    '''


if __name__ == '__main__':
    add()
