from flask import Blueprint,session,render_template
index_bp = Blueprint('index',__name__)
@index_bp.route('/index')
def index():
    if 'logged_in' in session:
          return render_template('index.html')
    return render_template('login.html')