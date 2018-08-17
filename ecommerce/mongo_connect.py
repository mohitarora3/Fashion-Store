from flask import Flask 
from flask_pymongo import PyMongo

app=Flask(__name__)

#app.config['MONGO_DBNAME']='connect_to_mongo'
app.config['MONGO_URI']="mongodb://localhost:27017/myDatabase"

#app.config['MONGO_URI']='mongodb://MohitArora:mohit003@ds119422.mlab.com:19422/connect_to_mongo'

mongo=PyMongo(app)

@app.route('/add')
def add():
	user=mongo.db.users
	user.insert( {'name' : 'lala'} )
	user.insert( {'name' : 'gulu'} )
	user.insert( {'name' : 'hulu'} )
	user.insert( {'name' : 'nulu'}, {'gender':'male'} )
	

	return 'addedd user'

if __name__=='__main__':
	app.run(debug=True)