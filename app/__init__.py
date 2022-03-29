from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kgisl_iim.sqlite3'
db = SQLAlchemy(app)

from app import route
from app import db_script