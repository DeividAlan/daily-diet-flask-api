from flask import Blueprint, request, jsonify
from models.user import User
from flask_login import login_user, logout_user
import bcrypt

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            return jsonify({"message": "User authorized!"})
    
    return jsonify({"message": "Invalid username or password!"}), 404

@auth_routes.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return jsonify({"message": "You have been successfully logged out."})