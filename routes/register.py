from flask import Blueprint,render_template, request, redirect, url_for, session
from extension import db,User,bcrypt

register_bp = Blueprint('register',__name__)
@register_bp.route('/register',methods=['GET','POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')
    if request.method =='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        card_number = request.form['card_number']
        en_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User()
        new_user.username = username
        new_user.email = email
        new_user.password = en_password
        new_user.card_number = card_number
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
