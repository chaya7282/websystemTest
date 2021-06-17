from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# This is a sample Python script.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import flask_sqlalchemy
import sqlalchemy.dialects.postgresql
from sqlalchemy.dialects import postgresql
import os
from flask import render_template, url_for, flash, redirect, request, abort
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, FormField, IntegerField
from flask_wtf.file import FileField, FileAllowed,  FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import FlaskForm

app = Flask(__name__)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_RECORD_QUERIES = True
app.config['SECRET_KEY'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://qbsdrpzncxfnwl:76154e16537f644b775dbe31717f9016960b8492725cc3fd7f7415ef5856f7ce@ec2-3-212-75-25.compute-1.amazonaws.com:5432/d7den0ai7rfc4a'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)