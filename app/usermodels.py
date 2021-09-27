from app.app import db
from mongoengine import StringField

class User(db.Document):
    username = db.StringField(required = True)
    email = db.StringField(required = True, unique = True)
    password = db.StringField(required = True)
    usertype = db.StringField(required = True)

    def is_authentiacted(self):
        return True

    def get_id(self):
        return str(self.id)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_role(self):
        return self.get.role

    def check_role(self, roles):
        return self.roles in roles