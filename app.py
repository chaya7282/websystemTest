#from flask import Flask
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
from webTest import app,db
from webTest.models import Product2


class ProductForm(FlaskForm):

    company = StringField('What is the company name?', validators=[DataRequired()])
    name = StringField('What is the product name?', validators=[DataRequired()])
    description = TextAreaField('Give a product description', validators=[DataRequired()])
    price = IntegerField('What is the price?', validators=[DataRequired()])
    picture = FileField('Product Picture',validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

    submit = SubmitField('Post')




if __name__ == '__main__':
    app.run()