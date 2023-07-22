from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user, UserMixin
from . import db


main = Blueprint('main', __name__)
if __name__=='__main__':
    app.run(debug=True)

@main.route('/')
def index():
    #return render_template('index.html')
    return redirect(url_for('views.home'))

#@main.route('/profile')
#@login_required
#def profile():
#    return render_template('profile.html', name=current_user.name)

@main.route('/your-profile')
def your_profile():
    return render_template('profilee.html', name=current_user.name, email=current_user.email, password=current_user.password)