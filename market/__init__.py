from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b303366d7cc1afd485c2274f'
db = SQLAlchemy(app)
from market import routes


# @app.route('/')
# def hello_world():
#     return '<h1>Hello ,world!!</h1>'

# @app.route('/about/<username>')
# def about(username):
#     return f'<h1> This is a about page of {username}</h1>'
