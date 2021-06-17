from datetime import datetime
from webTest import db
from flask_login import UserMixin

from sqlalchemy import DateTime
from sqlalchemy import event
import enum
from sqlalchemy import Integer, Enum


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', uselist=False, back_populates="cart")


class Order(db.Model):
    """An order placed by a customer, composed of Order-Quantities"""

    __tablename__ = "order"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)



class Store(db.Model):
    __tablename__ = 'store'
    id = db.Column(db.Integer(), primary_key=True)
    product = db.relationship('Product', uselist=False, back_populates="store")


class Role(db.Model):
    __tablename__ = 'Roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship('User', secondary='UserRoles', backref=db.backref("role", lazy="dynamic"))
   # # Define the UserRoles association table


class UserRole(db.Model):
    __tablename__ = 'UserRoles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('Roles.id', ondelete='CASCADE'))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'))
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(60), nullable=False)
    roles = db.relationship('Role', secondary='UserRoles', backref=db.backref('user', lazy='dynamic'))


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company= db.Column(db.String(20), nullable=False)
    name= db.Column(db.String(20), nullable=False)
    description= db.Column(db.Text, nullable=True)
    price= db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    time_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    group_type=  db.Column(db.String(20), nullable=False, default='All')
    is_active = db.Column(db.Boolean,default=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    store = db.relationship("Store", back_populates="product")
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    cart = db.relationship("Cart", back_populates="product")

class Product2(db.Model):
    __tablename__ = 'product2'
    id = db.Column(db.Integer, primary_key=True)
    company= db.Column(db.String(20), nullable=False)
    name= db.Column(db.String(20), nullable=False)
    description= db.Column(db.Text, nullable=True)
    price= db.Column(db.Integer, nullable=False)
    group_type=  db.Column(db.String(20), nullable=False, default='All')


class ActiveOrders(db.Model):
    __tablename__ = 'activeOrders'
    id = db.Column(db.Integer(), primary_key=True)

class ShoppingCart(db.Model):
    __tablename__ = 'shoppingCart'
    id = db.Column(db.Integer(), primary_key=True)