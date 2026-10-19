from flask import Blueprint, request, render_template, redirect, url_for
import time
import routes.login as login_state

otp_bp = Blueprint('otp', __name__)

@otp_bp.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'GET':
        if login_state.a < 4 and time.time() - login_state.t1 < 60:
            return render_template('otp.html')
        else:
            login_state.t1 = 0
            login_state.a = 0
            return redirect(url_for('login'))

    if request.method == 'POST':
        login_state.a = login_state.a + 1
        otp = request.form['otp']
        if otp == str(login_state.get_otp):
            login_state.a = 0
            if time.time() - login_state.t1 < 60:
                login_state.t1 = 0
                return render_template('index.html')

    return redirect(url_for('otp'))


