from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app , os

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ouzeon@localhost:5432/flaskdb?client_encoding=utf8'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db', 'flaskdb2.sqlite3')


db = SQLAlchemy(app)
migrate = Migrate(app, db)