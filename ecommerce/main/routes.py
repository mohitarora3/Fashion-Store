from flask import Blueprint, render_template
from ecommerce import mongo
from flask_login import current_user
from bson.objectid import ObjectId
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    items = mongo.db.items.find_one_or_404()
    return render_template('home.html', item=items)


@main.route('/item/<string:item_id>')
def item(item_id):
    item = mongo.db.items.find_one_or_404({"_id": ObjectId(item_id)})
    return render_template('item.html', item=item, title=item['Description'])
