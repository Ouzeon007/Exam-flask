from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import IntegerField, StringField,FloatField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired, length

class ProductForm(FlaskForm):
  libelle = StringField('libelle',validators=[InputRequired(message='le libelle est obligatoire'), length(min=3, max=50, message='le libelle doit être entre 3 et 50 caractères')])
  prix = FloatField('prix',validators=[InputRequired(message='le prix est obligatoire')])
  qteStock = IntegerField('qteStock',validators=[InputRequired(message='la quantité en stock est obligatoire')])
  description = StringField('description',validators=[InputRequired(message='la description est obligatoire')])
  img = FileField(validators=[FileRequired(message='le fichier est obligatoire')])

class UserForm(FlaskForm):
  username = StringField('username',validators=[InputRequired(message='le username est obligatoire'), length(min=3, max=50, message='le username doitêtre entre 3 et 50 caractères')])
  password = StringField('password',validators=[InputRequired(message='le password est obligatoire'), length(min=3, max=50, message='le password doitêtre entre 3 et 50 caractères'),])
  