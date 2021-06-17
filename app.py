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


app = Flask(__name__)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_RECORD_QUERIES = True
app.config['SECRET_KEY'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b8ff07330af1f1:c66beaa7@us-cdbr-east-04.cleardb.com/heroku_e7818c97bf7c572'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:chaya@localhost/chayadb'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class ProductForm(FlaskForm):

    company = StringField('What is the company name?', validators=[DataRequired()])
    name = StringField('What is the product name?', validators=[DataRequired()])
    description = TextAreaField('Give a product description', validators=[DataRequired()])
    price = IntegerField('What is the price?', validators=[DataRequired()])
    picture = FileField('Product Picture',validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

    submit = SubmitField('Post')


class Product2(db.Model):
    __tablename__ = 'product2'
    id = db.Column(db.Integer, primary_key=True)
    company= db.Column(db.String(20), nullable=False)
    name= db.Column(db.String(20), nullable=False)
    description= db.Column(db.Text, nullable=True)
    price= db.Column(db.Integer, nullable=False)
    group_type=  db.Column(db.String(20), nullable=False, default='All')





@app.route("/products")

#@requires_roles('Admin','Agent')
def products():
    products = Product2.query.all()
    print(len(products))

    return render_template('test5.html',products=products)




@app.route('/', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if request.method == 'POST':
       # picture_file = save_picture(form.picture.data)
       # image_file= url_for('static', filename='profile_pics/' + picture_file)
        select = request.form.get('group_products')
        product = Product2(company=form.company.data, name=form.name.data,
                          description=form.description.data, price= form.price.data,group_type=select)
        db.session.add(product)
        product.company=form.company.data
        db.session.commit()
    else:
        return render_template('add_product.html', title='add_product', form=form)

    return redirect(url_for('products'))


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()