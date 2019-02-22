from ecommerce import db, login_manager, mongo
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from bson.objectid import ObjectId
from flask_admin.contrib.pymongo import ModelView, filters

#from flask_admin.contrib.mongoengine import ModelView


class User(UserMixin, db.Document):
    #meta = {'collection': 'users'}
    #meta = {'DB': 'myDatabase'}
    username = db.StringField(max_length=30)
    email = db.EmailField(max_length=30)
    password = db.StringField()
    role = db.StringField()
    approved = db.BooleanField()
    isactive = db.BooleanField()
    item = db.StringField()
    wishlist = db.StringField()
    list_address = db.StringField()

    def __rep__(self):
        return 'User({},{})'.format(self.username, self.email)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        print('Serializer working',type(self.id))
        #print(ObjectId(self.get_id).valueOf())
        print('noooooooooooooooooo',self.id,'       ',self.get_id())
        return s.dumps({'user_id': str(self.get_id())}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        print(type(user_id))
        print('yesssssssssssssssssssssssssssss   ',user_id)
        return User.objects(pk=ObjectId(user_id)).first()

# with switch_db(User, 'archive') as User:
# User(name='Ross').save()  # Saves the 'archive-user-db'
'''
hashpass = generate_password_hash("mohitarora123", method='sha256')
role = 'admin'
User("Mohit Arora","arora3mohit@gmail.com",hashpass,role).save()
'''
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User

'''
class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')
    form = User


aadmin.add_view(ModelView(User))

'''
#admin.add_view(ModelView(Post, db.session))
# Admin.add_view(UserView(User))

