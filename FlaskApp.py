from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, logging, request
from passlib.hash import sha256_crypt
from functools import wraps

import os

from users import Users
from serialize import Serialize
from web.register import Register
from db import Db
password = "qwerty"
username = "admin"

userList = Users()
userList = Serialize.loadJSON()


app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('You must be logged in to enter this page!', 'danger')
            return index()
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
 
@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == password and request.form['username'] == username:
        session['logged_in'] = True
    else:
        flash('You typed wrong password!', 'danger')
    return index()

@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    flash('You are logged out!', 'info')
    return index()

@app.route('/users')
def users():
    return render_template('users.html', users = userList.getUserList())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register(request.form)
    
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surrname = form.surrname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #mysql
        Users.addUser(username, email, password, name, surrname)
        
        flash('Registration succesfull, now you can log in', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)