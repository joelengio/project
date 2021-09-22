from flask import Flask, request, jsonify
from app.app import db

class User():
    user = {
        "username": request.form.get("username"),
        "email": request.form.get("email"),
        "password": request.form.get("password1") 
    }
    db.users.insert_one(user)