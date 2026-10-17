from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import time
import urllib.parse
from random import randint
from dotenv import load_dotenv
load_dotenv()

import os



app = Flask(__name__)
app.config['SECRET_KEY'] =os.getenv('SECRET_KEY')
raw_password =os.getenv('PASSWORD')
password=urllib.parse.quote(raw_password)
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://root:{password}@localhost:3306/AUTHENTICATION'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ky3995018@gmail.com'
app.config['MAIL_PASSWORD'] ='zmxxbhnmrxlyzdto'
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
get_otp =""
a=0
t1 =0



class User(db.Model):
    __tablename__ = 'kamal'
    id =db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(456),unique=True,nullable =False)
    email =db.Column(db.String(456),unique =True,nullable =False)
    password = db.Column(db.String(456),unique=True,nullable =False)
    card_number = db.Column(db.String(80),unique =True,nullable =False)


@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        card_number = request.form['card_number']
        en_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(
        username = username,
        email = email,
        password = en_password,
        card_number = card_number

    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))



@app.route('/login',methods = ['GET','POST'])
def login():
    global get_otp
    global a
    global t1

    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_data = db.session.scalar(db.select(User).where(User.email == email))
        if bcrypt.check_password_hash(user_data.password, password):
            session['logged_in']=email
            get_otp =randint(100000,999999)
            t1 = time.time()
            msg = Message(f'Your one time password is sent to your email {email}',sender ='ky3995018@gmail.com',recipients=[email])
            msg.body =str(get_otp)
            mail.send(msg)


            return redirect(url_for('otp'))
        return render_template('login.html')

@app.route('/index')
def index():
    if 'logged_in' in session:
          return render_template('index.html')
    return render_template('login.html')
@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
        return redirect('login')
@app.route('/delete')
def delete():
    if 'logged_in' in session:
        delete_user = db.session.scalar(db.select(User).where(User.email == session['logged_in']))
        db.session.delete(delete_user)
        db.session.commit()
        return render_template('register.html')

@app.route('/otp',methods=['GET','POST'])
def otp():

    global a
    global get_otp
    global t1

    if request.method == 'GET':
        if a < 4 and time.time()-t1 < 60 :
            return render_template('otp.html')
        else :
            t1 =0
            a=0
            return redirect(url_for('login'))

    if request.method == 'POST':
        a = a+1
        otp = request.form['otp']
        if otp == str(get_otp):
            a=0
            if time.time()-t1 < 60:
                 return render_template('index.html')
                 t1 =0

    return redirect(url_for('otp'))



            






if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0',port=5007)







