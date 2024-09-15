from flask import Blueprint, request, jsonify
from models.meal import Meal
from database import db
from flask_login import login_required, current_user

meal_routes = Blueprint('meal_routes', __name__)

@meal_routes.route("/meal", methods=["POST"])
@login_required
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")
    in_diet = data.get("in_diet")

    if name and date_time is not None and in_diet is not None:
        new_meal = Meal(
            name=name,
            description=description,
            date_time=date_time,
            in_diet=in_diet,
            user_id=current_user.id
        )
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({"message": "Meal created successfully!"}), 201
    
    return jsonify({"message": "Name, date_time, and in_diet are required!"}), 400

@meal_routes.route("/meal/<int:meal_id>", methods=["PUT"])
@login_required
def update_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal:
        if meal.user_id != current_user.id:
            return jsonify({"message": "You are not authorized to update this meal."}), 403
        
        data = request.json
        name = data.get("name")
        description = data.get("description")
        date_time = data.get("date_time")
        in_diet = data.get("in_diet")

        if name is not None:
            meal.name = name
        if description is not None:
            meal.description = description
        if date_time is not None:
            meal.date_time = date_time
        if in_diet is not None:
            meal.in_diet = in_diet
        db.session.commit()
        return jsonify({"message": "Meal updated successfully!"}), 200

    return jsonify({"message": "Meal not found!"}), 404


@meal_routes.route("/meal/<int:meal_id>", methods=["DELETE"])
@login_required
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal:
        if meal.user_id != current_user.id:
            return jsonify({"message": "You are not authorized to delete this meal."}), 403
        
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully!"}), 200

    return jsonify({"message": "Meal not found!"}), 404

@meal_routes.route("/meal/<int:meal_id>", methods=["GET"])
@login_required
def read_meal(meal_id):
    meal = Meal.query.get(meal_id)

    print(meal.user_id)
    print(current_user.id)

    if meal and meal.user_id == current_user.id:        
        return jsonify({
            "message": "Meal deleted successfully!",
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time.isoformat(),
            "in_diet": meal.in_diet
        })
    
    return jsonify({"message": "Meal not found!"}), 404

@meal_routes.route("/meals", methods=["GET"])
@login_required
def read_meals():
    meals = Meal.query.filter_by(user_id=current_user.id).all()

    return jsonify({"meals": [meal.to_dictionary() for meal in meals]})