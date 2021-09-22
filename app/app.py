from flask import Flask
import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfg'

client = pymongo.MongoClient('localhost' ,27017)
db = client.user_data
