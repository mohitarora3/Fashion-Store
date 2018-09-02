from flask import Flask
from flask_pymongo import PyMongo
import pprint

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"


mongo = PyMongo(app)


def add():
    item_id = 'knfkn'
    mongo.db.user.update({"_id": ObjectId("5b7ef8f3ba58e927aebafb72")}, {$set: {"cart_item_ids": item_id}})
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
