from flask import render_template, url_for, flash, redirect, request, abort
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, FormField, IntegerField
from flask_wtf.file import FileField, FileAllowed,  FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import FlaskForm
from webTest import app,db
from webTest.models import Product


class ProductForm(FlaskForm):

    company = StringField('What is the company name?', validators=[DataRequired()])
    name = StringField('What is the product name?', validators=[DataRequired()])
    description = TextAreaField('Give a product description', validators=[DataRequired()])
    price = IntegerField('What is the price?', validators=[DataRequired()])
    picture = FileField('Product Picture',validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

    submit = SubmitField('Post')




@app.route("/products")

#@requires_roles('Admin','Agent')
def products():
    products = Product.query.all()
    print(len(products))

    return render_template('test5.html',products=products)




@app.route('/', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if request.method == 'POST':
       # picture_file = save_picture(form.picture.data)
       # image_file= url_for('static', filename='profile_pics/' + picture_file)
        select = request.form.get('group_products')
        product = Product(company=form.company.data, name=form.name.data,
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

