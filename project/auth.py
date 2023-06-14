from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from project.models.users import User

from . extensions import db, bcrypt

auth = Blueprint('auth', __name__)
#bcrypt = Bcrypt(auth)


@auth.route('/login')
def login():
    """ route for login page """
    return (render_template('login.html'))

@auth.route('/login', methods=['POST'])
def login_post():
    """ route that filters the request form
        check the database to valid if the input
        data from the form is on the database
    """
    email = request.form.get('email')
    password = request.form.get('passsword')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user exists by taking the
    # the password, hash it and compare it with the hashed one saved
    #if not user or not bcrypt.check_password_hash(user.password, password):
    if not user or not user.password:
        flash('Email or Password supplied is not correct')
        return (redirect(url_for('auth.login')))
    login_user(user, remember=remember)
    return redirect(url_for('main.newsfeed'))

@auth.route('/signup')
def signup():
    # route that handles the signup page
    return (render_template('signup.html'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    """ route that get the input from the form
        check if the input is already on the database
        if not store the input on the database
    """
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    # check if email already exist
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email already used')
        return (redirect(url_for('auth.signup')))

    # Create a new user hash the password no to store it in a plain text
    new_user = User(email=email, name=name, password=password)
    #new_user = User(email=email, name=name, password=bcrypt.generate_password_hash(password).decode('utf-8'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    # redirect to the auth.login page
    return (redirect(url_for('auth.login')))


@auth.route('/profile')
@login_required
def profile():
    """ A route that the users profile """ 
    name = current_user.name
    # query the user by email
    
    return ( render_template('profile.html',user=name))
    

@auth.route('/logout')
@login_required
def logout():
    # logout route
    logout_user()
    return (redirect(url_for('main.index')))


