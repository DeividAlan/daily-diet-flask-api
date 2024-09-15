from flask import Flask
from database import db
from flask_login import LoginManager
from config import Config
from models.user import User
from routes.auth import auth_routes
from routes.meal import meal_routes
from routes.user import user_routes

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

# Register blueprints
app.register_blueprint(auth_routes)
app.register_blueprint(meal_routes)
app.register_blueprint(user_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se ainda não existirem
    app.run(debug=True)