from flask import render_template, redirect, url_for, request, flash
from app.app import app
from app.app import db
from app.usermodels import User
from app.app import login_manager

from flask_login import login_user, logout_user, current_user

def home():
    return render_template('index.html')

def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.objects.get(email = email)
        if user:
            if user.password == password:
                flash("You've been logged In")
                return render_template("profile.html", email = user.email, username = user.username)
                
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

def profile():
    
    return render_template("profile.html")

def food():
    return render_template("food.html")

#routes
app.add_url_rule("/", view_func=home, methods= ["GET","POST"])
app.add_url_rule("/login", view_func=login, methods= ["GET","POST"])
app.add_url_rule("/register", view_func=register, methods= ["GET","POST"])
app.add_url_rule("/logout", view_func=logout, methods= ["GET","POST"])
app.add_url_rule("/profile", view_func = profile , methods =["GET"])
app.add_url_rule("/food", view_func = food , methods =["GET","POST"])