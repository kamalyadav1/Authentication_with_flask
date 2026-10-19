from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()


class User(db.Model):
    __tablename__ = 'kamal'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(456), unique=True, nullable=False)
    email = db.Column(db.String(456), unique=True, nullable=False)
    password = db.Column(db.String(456), unique=True, nullable=False)
    card_number = db.Column(db.String(80), unique=True, nullable=False)