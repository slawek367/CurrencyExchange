from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, logging, request
from passlib.hash import sha256_crypt
from functools import wraps

import os

from users import Users
from wallet import Wallet
from update import Update
from web.register import Register
from db import Db
password = "qwerty"
username = "admin"

app = Flask(__name__)
update = Update()
update.updatePrices()

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
    return render_template('index.html')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == password and request.form['username'] == username:
            session['admin_logged_in'] = True
            return index()
        elif Users.checkLoginAndPassword(request.form['username'], request.form['password']):
            session['logged_in'] = True
            session['user_name'] = Users.getUser(username = request.form['username'], email = request.form['username']).getName()
            session['user_id'] = Users.getUser(username = request.form['username'], email = request.form['username']).getId()
            return index()
        else:
            flash('You typed wrong username/email or password!', 'danger')
            return render_template('login.html')
    else:
        return render_template('login.html')
        

@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    session['user_name'] = None
    session['user_id'] = None
    flash('You are logged out!', 'info')
    return index()

@login_required
@app.route('/wallet')
def wallet():
    if 'user_id' in session.keys():
        wallet = Wallet(session['user_id'])
    else:
        return index()

    return render_template('wallet.html', wallet = wallet)

@login_required
@app.route('/market')
def market():
    if 'user_id' in session.keys():
        wallet = Wallet(session['user_id'])
    else:
        return index()

    return render_template('market.html', wallet = wallet)

@app.route('/users')
def users():
    return render_template('users.html', users = Users.getUserList())

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
        password = form.password.data

        #mysql
        Users.addUser(username, email, password, name, surrname)
        
        flash('Registration succesfull, now you can log in', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
    #app.run(debug=False,host='0.0.0.0', port=4000)