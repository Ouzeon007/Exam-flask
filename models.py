from sqlalchemy import Column, Integer, String, Boolean

from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from application.routes import redirect, url_for,UserMixin


from config import db


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    prix = Column(Integer)
    img = Column(String ,unique=True)
    description = Column(String)

    def __init__(self,title, prix,img, description=""):
        self.title = title
        self.prix = prix
        self.img = img
        self.description = description
    
    def __repr__(self):
        return f"<Product {self.title}>"
    

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    qteStock = Column(Integer, default=0)
    is_admin = Column(Boolean, default=0)

    def __init__(self,username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return f"<User {self.username}>"
    

# class SecureModelView(ModelView):
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.is_admin

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('login'))
    
