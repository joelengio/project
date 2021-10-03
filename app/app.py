from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfg'
app.config["MONGODB_SETTINGS"] = {
    "db": "user_data",
    "host" : "localhost",
    "port" : 27017
}
db = MongoEngine(app)

login_manager = LoginManager()

