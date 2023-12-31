from flask_login import login_user, login_required, logout_user, current_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')



@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods = ['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user:
        flash('email already exists')
        return redirect(url_for('auth.signup'))


    else:
        new_user = User(email = email, name = name, password = generate_password_hash(password, method = 'sha256'))

        db.session.add(new_user)
        db.session.commit()

        #login_user(new_user, remember = True)
        flash ('Account create!')
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.login'))



@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('incorrect password')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.your_profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


#@auth.route('/telecommunication-engineering')
#def tc():
#    return render_template ('Telecommunication-engineering.md')
