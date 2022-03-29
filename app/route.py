from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.db_script import Users

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/index.html')
def index ():
    return render_template('index.html')

@app.route('/register.html', methods = ['GET', 'POST'])
def register ():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            User = Users(name = request.form['name'], email = request.form['email'], password = request.form['password'])
            
            db.session.add(User)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('testing_db.html'))

    return render_template('testing_db.html')

@app.route('/login.html')
def login ():
    return render_template('login.html')

@app.route('/about.html')
def about ():
    return render_template('about.html')

@app.route('/contact.html')
def contact ():
    return render_template('contact.html')

@app.route('/engagement.html')
def engagement ():
    return render_template('engagement.html')

@app.route('/testing_db.html')
def testing_db ():
    return render_template('testing_db.html', Users = Users.query.all() )
