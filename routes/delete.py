from flask import Blueprint, session, render_template, redirect, url_for
from extension import User, db
delete_bp = Blueprint('delete', __name__)
@delete_bp.route('/delete')
def delete():
    if 'logged_in' in session:
        delete_user = db.session.scalar(db.select(User).where(User.email == session['logged_in']))
        if delete_user:
            db.session.delete(delete_user)
            db.session.commit()
        session.pop('logged_in', None)
        return render_template('register.html')
    return redirect(url_for('login'))