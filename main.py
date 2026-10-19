from flask import Flask, render_template, request, redirect, url_for, session

import time
import urllib.parse
from random import randint
from dotenv import load_dotenv
from extension import db, bcrypt, mail, User
from routes import register_routes

load_dotenv()

import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.getenv('SECRETE_KEY')
raw_password = os.getenv('PASSWORD') or ''
password = urllib.parse.quote(raw_password)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost:3306/AUTHENTICATION'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ky3995018@gmail.com'
app.config['MAIL_PASSWORD'] = 'zmxxbhnmrxlyzdto'
app.config['MAIL_USE_SSL'] = False

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
mail.init_app(app)

# Register routes via routes manager
register_routes(app)














            






if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0',port=5007)







