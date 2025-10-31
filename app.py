import os
import bcrypt
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_login import login_required, login_user, logout_user, current_user
from database import db
from model.food import Food
from model.user import User
from flask_login import login_manager, LoginManager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_DATABASE_URI')

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and password:
            login_user(user)
            return jsonify({'message': 'Logged in successfully'})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@app.route('/user', methods=['POST'])
@login_required
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User.query.filter_by(username=current_user.username).first()
        new_user = User(username=username, password=hashed_password, role=role if not None else 'user')
        if User.query.filter_by(username=username).first():
            return jsonify({"message": "User already exists"}), 400
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Succesfully registered user"})
    return jsonify({"message": "Invalid data"}), 400

@app.route('/user/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    return jsonify({"message": "User not found!"}), 404

@app.route('/user/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found!"}), 404
    if user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 401
    
    password = data.get('password')
    if password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user.password = hashed_password

    db.session.commit()
    return jsonify({"message": f"Password of user {user.username} update successfully"})

@app.route('/user/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found."}), 404
    if user.id == current_user.id:
        return jsonify ({"message": "The user cannot delete himself"}), 403
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user.username} deleted successfully"})    


@app.route('/food', methods=['POST'])
@login_required
def create_food():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    eated_at = data.get('eated_at')
    on_diet = data.get('on_diet')

    user = current_user

    if not user:
        return jsonify({ "message": "Unauthorized"}), 401

    if title and description:
        new_food = Food(title=title, description=description, eated_at=eated_at, on_diet=on_diet, user_id=user.id)
        db.session.add(new_food)
        db.session.commit()
        return jsonify({"message": f"Add Food successfully"})
    return jsonify({"message": "Failure to add Food"})


@app.route('/food', methods=['GET'])
def get_food():
    foods = Food.query.filter_by(user_id=current_user.id).all()
    foods_list = []

    for food in foods:
        foods_list.append({
            'title': food.title,
            'description': food.description,
            'eated_at': food.eated_at.strftime('%d-%m-%Y %H:%M:%S'),
            'on_diet': food.on_diet
        })

    return jsonify(foods_list)

@app.route('/food/<int:food_id>', methods=['GET'])
def get_food_by_id(food_id):
    food = Food.query.get(food_id)
    if food:
        return jsonify ({'title': food.title, 'description': food.description, 'eated_at': food.eated_at.strftime('%d-%m-%Y %H:%M:%S'), 'on_diet': food.on_diet })
    
@app.route('/food/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    data = request.get_json()
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"message": "Food not found"}), 404
    
    title = data.get('title')
    description = data.get('description')
    on_diet = data.get('on_diet')
    if title and description and on_diet:
        food.title = title
        food.desctiption = description
        food.on_diet = on_diet
    
    db.session.commit()
    return jsonify({"message": "Update successfully"})

@app.route('/food/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = Food.query.get(food_id)
    
    if not food:
        return jsonify({"message": "Food not found."}), 404 
    if food.user_id != current_user.id:
        return jsonify({"message": "Unauthorized."}), 401 
    db.session.delete(food)
    db.session.commit()
    return jsonify({"message": f"Food {food.title} deleted sucessfully"})
     

if __name__ == '__main__':
    app.run(debug=True)