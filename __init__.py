from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# This is a sample Python script.
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import flask_sqlalchemy
import sqlalchemy.dialects.postgresql
from sqlalchemy.dialects import postgresql
import os


app = Flask(__name__)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_RECORD_QUERIES = True
app.config['SECRET_KEY'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b8ff07330af1f1:c66beaa7@us-cdbr-east-04.cleardb.com/heroku_e7818c97bf7c572'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:chaya@localhost/chayadb'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

