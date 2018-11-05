from flask import Blueprint, render_template, jsonify, request
from ecommerce import mongo
from flask_login import current_user
from bson.objectid import ObjectId
import json
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
  items = mongo.db.items
  return render_template('home.html', items=items)


@main.route('/item/<string:item_id>')
def item(item_id):
  item = mongo.db.items.find_one_or_404({"_id": ObjectId(item_id)})
  reviews_exist = mongo.db.review.find({'item_id': ObjectId(item_id)}, {'_id': 0, 'reviews': 1}).count()
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
  return render_template('item.html', item=item, reviews_cursor=reviews_dict_cursor, title=item['Description'])


@main.route('/search_results', methods=['POST'])
def search():
  search_input = request.form['search']
  search_result_count = mongo.db.items.find({'$text': {'$search': search_input}}).count()
  if search_result_count:
    search_results = mongo.db.items.find({'$text': {'$search': search_input}})
  else:
    search_results = None
  return render_template('search.html', count=search_result_count, search_results=search_results)


@main.route('/seller')
def seller():
  return render_template('sellerdashboard.html')
