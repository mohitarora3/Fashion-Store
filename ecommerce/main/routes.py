from flask import Blueprint, render_template, jsonify, request
from ecommerce import mongo
from flask_login import current_user
from bson.objectid import ObjectId
import json
from bson.json_util import dumps

main = Blueprint('main', __name__)
global gender
gender = None


def ret_brands(Category=None, Type=None):
  if(Category != None and Type != None):
    brands = mongo.db.items.distinct('Brand', {'Category': Category, 'Type': Type})
  elif(Category != None):
    brands = mongo.db.items.distinct('Brand', {'Category': Category})
  else:
    brands = mongo.db.items.distinct('Brand', {'Type': type})

  return brands


def ret_categories(category):
  categories = mongo.db.items.distinct('Type', {'Category': category})
  return categories


@main.route('/items/gender', methods=['POST'])
def update_home():
  gender = request.json
  categories = ret_categories(gender)
  #items = mongo.db.items.find({'Category': gender})
  brands = ret_brands(gender)
  return render_template('categories_brands.html', brands=brands, categories=categories,gender=gender)


@main.route('/', defaults={'type': 'Shirt'})
@main.route('/<string:type>')
def home(type):
  mongo.db.items.find_one_or_404({'Type': type.title()})  # just to return 404 error if there is not a single item with that thing
  items = mongo.db.items.find({'Type': type.title()})
  global itemType
  itemType = type  # so that same type of items are getched in filter results
  brands = ret_brands(type)
  categories = ret_categories('Men')
  types = mongo.db.items.distinct('Type')
  return render_template('home.html', items=items, brands=brands, categories=categories, itemType=type.title(), types=types)


@main.route('/newhome')
def newhome():
  itemsb = mongo.db.items.find({'Type': 'Bedsheet'}).limit(12)
  itemst = mongo.db.items.find({'Type': 'Top'}).limit(12)
  itemsd = mongo.db.items.find({'Type': 'Dress'}).limit(12)
  itemss = mongo.db.items.find({'Type': 'Shirt'}).limit(12)

  return render_template('newhome.html', itemsb=itemsb, itemst=itemst, itemsd=itemsd, itemss=itemss)


@main.route('/items/filter', methods=['POST'])
def filter():
  minDiscount = 0
  maxPrice = 10000
  print('here')

 # print(request.json)
  brands = request.json['Brand']
  types = request.json['Type']

  Gender=request.json['Gender']


  print('brands: ', len(brands))
  if(request.json["Price"]):
    maxPrice = 100
    for price in request.json['Price']:
      maxPrice = max(maxPrice, price)
  if(request.json["Discount"]):
    minDiscount = 100
    for discount in request.json['Discount']:
      minDiscount = min(minDiscount, discount)
  print('maxPrice is ', maxPrice)
  if(len(Gender)==0 and len(types) == 0 and len(brands)==0 ):
     items = mongo.db.items.find(
      {'$and': [
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  if(len(Gender)==0 and len(types) == 0 and len(brands)!=0):
     items = mongo.db.items.find(
      {'$and': [
          {'$or': brands},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(len(Gender)==0 and len(types)!=0 and len(brands)==0 ):
    print('dogy')
    items = mongo.db.items.find(
      {'$and': [
          {'$or': types},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(len(Gender)==0 and len(types)!=0 and len(brands)!=0):
     items = mongo.db.items.find(
      {'$and': [
          {'$or': types},
          {'$or': brands},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(len(Gender)!=0 and len(types)!=0 and len(brands)==0 ):
     items = mongo.db.items.find(
      {'$and': [
          {'Category': gender},
          {'$or':types},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(Gender is not  None and len(types)!=0 and len(brands)!=0):
     items = mongo.db.items.find(
      {'$and': [
          {'Category': Gender},
          {'$or':types},
          {'$or':brands},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(len(Gender)!=0 and len(types) == 0 and len(brands)==0 ):
    print('entering')
    items = mongo.db.items.find(
      {'$and': [
          {'Category': Gender},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  elif(len(Gender)!=0 and len(types) == 0 and len(brands)!=0):
    print('yippy')
    print(gender)
    items = mongo.db.items.find(
      {'$and': [
          {'Category': Gender},
          {'$or':brands},
          {'Price': {'$lte': maxPrice}},
          {'Discount': {'$gte': minDiscount}}
      ]
      })

  return render_template('home_items.html', items=items)
  # return(dumps(items))


@main.route('/item/<string:item_id>')
def item(item_id):
  item = mongo.db.items.find_one_or_404({"_id": ObjectId(item_id)})
  reviews_exist = mongo.db.review.find({'item_id': ObjectId(item_id)}, {'_id': 0, 'reviews': 1}).count()
  similar_products = mongo.db.items.find({'Category': item['Category'], 'Type': item['Type']}).limit(10)
  if reviews_exist:
    reviews_dict_cursor = mongo.db.review.aggregate([{'$project':
                                                      {
                                                          'rating_avg': {'$avg': '$reviews.rating'},
                                                          'number': {'$size': '$reviews'},
                                                          'reviews': '$reviews'
                                                      }
                                                      }])
  else:
    reviews_dict_cursor = None
  return render_template('item.html', item=item, reviews_cursor=reviews_dict_cursor, title=item['Description'], similar_products=similar_products)


@main.route('/search_results', methods=['GET'])
def search():
  search_input = request.args.get("q")
  search_result_count = mongo.db.items.find({'$text': {'$search': search_input}}).count()
  if search_result_count:
    search_results = mongo.db.items.find({'$text': {'$search': search_input}})
  else:
    search_results = None
  return render_template('search.html', count=search_result_count, items=search_results)


@main.route('/seller')
def seller():
  return render_template('sellerdashboard.html')
