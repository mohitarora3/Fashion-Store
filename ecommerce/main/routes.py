from flask import Blueprint, render_template, jsonify
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
        reviews_dict = mongo.db.review.find_one({'item_id': ObjectId(item_id)}, {'_id': 0, 'item_id':1,'reviews': 1})
        reviews = reviews_dict['reviews']
    else:
        reviews = None
    return render_template('item.html', item=item, reviews=reviews, title=item['Description'])


@main.route('/seller')
def seller():
    return render_template('sellerdashboard.html')
