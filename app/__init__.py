from flask import render_template, redirect,url_for, request
from app.app import app
from app.app import db


def home():
    return render_template('index.html')

def login():
    return render_template('login.html')

def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = {
            "username":username,
            "email":email,
            "password":password1
        }
        db.users.insert_one(user)
        print(request.form)
        
    return render_template('register.html')

def logout():
    return redirect(url_for("home"))

#routes
app.add_url_rule("/", view_func=home)
app.add_url_rule("/login", view_func=login, methods=["GET","POST"])
app.add_url_rule("/register", view_func=register, methods=["GET","POST"])
app.add_url_rule("/logout", view_func=logout)