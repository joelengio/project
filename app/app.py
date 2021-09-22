from flask import Flask
import pymongo
from flask_login import LoginManager


app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = "qwerty"

#Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_data