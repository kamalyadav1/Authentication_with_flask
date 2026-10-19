from flask import Blueprint, session, redirect, url_for
logout_bp = Blueprint('logout', __name__)
@logout_bp.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect(url_for('login'))