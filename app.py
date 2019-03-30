from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from table_def import *
import pyrebase
engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)
app.secret_key = os.urandom(12)

config = {
  "apiKey": "AIzaSyCFiNl9jGE22lYQt9iSsBUIwOWvqEqBEMc",
  "authDomain": "hint-ec580.firebaseapp.com",
  "databaseURL": "https://hint-ec580.firebaseio.com",
  "storageBucket": "hint-ec580"
}

firebase = pyrebase.initialize_app(config)
 
@app.route('/')
def home():
    return render_template("home.html")
 
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin_login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email,password)
    if user:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged in'] = False
    return render_template('index.html')

if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0', port=4000)