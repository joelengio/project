from flask import render_template, redirect, url_for, request, flash
from app.app import app
from app.app import db

from flask_login import login_user, logout_user

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

def home():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.objects.get(email = email)
        if user:
            if user.password == password:
                login_user(user)
                return render_template("profile.html")
                flash("You've been logged In")
            else:
                flash("Password Incorrect")
        else:
            flash("Mail id not in use")

        
        
        
    return render_template('login.html')

def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        usertype = request.form.get("usertype")
        
        if password1 == password2:
            User.objects.create(username=username, password=password1, email = email , usertype = usertype)
            
            return redirect(url_for("login"))

        else:
            flash("passwords doesn't match")
        
        

    return render_template('register.html')

def logout():
    return redirect(url_for("home"))





#routes
app.add_url_rule("/", view_func=home, methods= ["GET","POST"])
app.add_url_rule("/login", view_func=login, methods= ["GET","POST"])
app.add_url_rule("/register", view_func=register, methods= ["GET","POST"])
app.add_url_rule("/logout", view_func=logout, methods= ["GET","POST"])