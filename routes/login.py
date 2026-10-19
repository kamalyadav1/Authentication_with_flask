from flask import Blueprint ,request,render_template,session,redirect,url_for
from flask_bcrypt import Bcrypt
from random import randint
from extension import User , db,bcrypt,mail
from flask_mail import Mail,Message
import time



get_otp = ""
a = 0
t1 = 0

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['GET', 'POST'])
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