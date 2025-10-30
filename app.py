import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_DATABASE_URI')

@app.route('/')
def home():
    return "Welcome to the Daily Diet API!"

if __name__ == '__main__':
    app.run(debug=True)