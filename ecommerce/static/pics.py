
from flask import Flask
from flask_pymongo import PyMongo

import pprint

i2 =
  {
      "Image": ['1.1.jpg', '1.2.jpg', '1.3.jpg', '1.4.jpg'],
      "Brand": "Highlander",
      "Short Description": "Slim Casual Shirt",
      "Description": "White Slim Fit Casual Shirt",
      "Mrp": "Rs. 999",
      "Discount": "45",
      "Price": "Rs. 549",
      "Size": ['38', '40', '42', '44'],
      "Product Details": "White casual shirt, has a spread collar, a full button placket, a patch pocket, long sleeves with roll-up button tabs, a curved hemline",
      "Material & Care": ['100% cotton', 'Machine-wash warm']
  },
  {
      "Image": ['2.1.jpg', '2.2.jpg', '2.3.jpg', '2.4.jpg'],
      "Brand": "Campus Sutra",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "Campus Sutra Men Blue Standard Regular Fit Self Design Casual Shirt",
      "Mrp": "Rs. 1399",
      "Discount": "65",
      "Price": "Rs. 489",
      "Size": ['38', '40', '42', '44'],
      "Product Details": "Blue self-design casual shirt, has a cutaway collar, button placket, 1 pocket, long sleeves, curved hem",
      "Material & Care": ['Cotton', 'Machine-wash']
  },
  {
      "Image": ['3.1.jpg', '3.2.jpg', '3.3.jpg', '3.4.jpg'],
      "Brand": "Hire&Now",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "HERE&NOW Men Grey & Black Regular Fit Checked Casual Shirt",
      "Mrp": "Rs. 1399",
      "Discount": "30",
      "Price": "Rs. 979",
      "Size": ['38', '40', '42', '44'],
      "Product Details": "Grey and black checked casual shirt, has a spread collar, button placket, 1 pocket, long sleeves, curved hem",
      "Material & Care": ['100% Cotton', 'Machine-wash']
  },
  {
      "Image": ['4.1.jpg', '4.2.jpg', '4.3.jpg', '4.4.jpg'],
      "Brand": "Nautica",
      "Short Description": "Men Regular Fit Casual Shirt",
      "Description": "Nautica Men Blue & Grey Regular Fit Checked Casual Shirt",
      "Mrp": "Rs. 2759",
      "Discount": "40% OFF",
      "Price": "Rs. 4599",
      "Size": ['38', '40', '42', '44'],
      "Product Details": "Blue and grey checked casual shirt, has a cutaway collar, button placket, 1 pocket, short sleeves, asymmetric hem",
      "Material & Care": ['Linen', 'Machine-wash']
  }
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
items = mongo.db.items
items.insert_one(i2)
pprint.pprint(items.find_one({"image": "2.2"}))
