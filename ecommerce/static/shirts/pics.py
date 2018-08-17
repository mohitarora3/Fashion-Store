
from flask import Flask
from flask_pymongo import PyMongo

import pprint
i1 = {
    "image": "1.2.jpg",
    "type": "shirt",
    "gender": "male",
    "description": "England Mens Checkered Casual Shirt",
    "price": "1599",
    "discount": "52",
    "Highlights":
    "['Fabric:Cotton','Slim Fit', 'Full Sleeve','Pattern: Checkered','Set of 1']",
        "Specifications":
    {"Pack of": "1",
     "Style Code": "ESF51702555DarkBrownWithWhite",
     "Closure": "Button",
     "Fit": "Slim",
     "Fabric": "Cotton",
     "SleeveFull": "Sleeve",
     "Pattern": "Checkered",
     "Reversible": "No",
     "Fabric Care": "Do not tumble dry, Do not bleach, Do not wring, Wash with like colors, Hand wash",
     "Suitable": "ForWestern Wear",
     "Pockets": "Patch Pocket at Front"}
}

i2 = {"Image": "['2.1.jpg','2.2.jpg','2.3.jpg','2.4.jpg']",
      "Brand": "Highlander",
      "Description": "White Slim Fit Casual Shirt",
      "Mrp": "Rs. 999",
      "Discount": "45% OFF",
      "Price": "Rs. 549",
      "Size": "['40','42','44']",
      "Product Details": "White casual shirt, has a spread collar, a full button placket, a patch pocket, long sleeves with roll-up button tabs, a curved hemline",
      "Material & Care": "['100% cotton', 'Machine-wash warm']"
      }
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
items = mongo.db.items
items.insert_one(i2)
pprint.pprint(items.find_one({"image": "2.2"}))
