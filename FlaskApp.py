from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

password = "qwerty"
username = "admin"
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged'):
        return render_template('login.html')
    else:
        return render_template('home.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == password and request.form['username'] == username:
        session['logged'] = True
    else:
        flash('You typed wrong password!')
    return home()
 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)