from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import pprint

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"


mongo = PyMongo(app)


def add():
    item_id = 'knfkn'
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
         {'cart_item_ids': ''}
         }

    )
    a = mongo.db.user.find_one({'email': 'mohit5@gmail.com'})
    print(a)

    print(a)
    '''
    items = mongo.db.items
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
