from flask import Blueprint, request, jsonify
from models.user import User
from database import db
from flask_login import login_required, current_user
import bcrypt

user_routes = Blueprint('user_routes', __name__)

@user_routes.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    
    return jsonify({"message": "Username and password are required!"}), 400

@user_routes.route("/user/<int:user_id>", methods=["GET"])
@login_required
def read_user(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify({ 
		    "id": user.id,
		    "username": user.username
		})
    
    return jsonify({"message": "User not found!"}), 404

@user_routes.route("/user/<int:user_id>", methods=["put"])
@login_required
def update_user(user_id):
    if user_id != current_user.id and current_user.role == 'user':
        return jsonify({"message": "You can't update the password for this user!"}), 403

    user = User.query.get(user_id)

    if user:
        data = request.json
        password = data.get("password")
        if password:
            user.password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
            db.session.commit()
            return jsonify({"message": "User updated!"})

        return jsonify({"message": "password is required!"}), 404

    return jsonify({"message": "User not found!"}), 404

@user_routes.route("/user/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return jsonify({"message": "You do not have permission to delete users!"}), 403

    if user_id == current_user.id:
        return jsonify({"message": "You cannot delete your own user account!"}), 403
    
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User {user_id} deleted!"})
    
    return jsonify({"message": "User not found!"}), 404