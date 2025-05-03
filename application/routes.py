from flask import Flask, render_template,request, redirect, url_for,flash,session
from werkzeug.utils import secure_filename
from application.forms import ProductForm, UserForm
from flask_wtf.csrf import CSRFProtect

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_login import LoginManager, login_user, logout_user, login_required,UserMixin

from app import app,os
from config import db
from models import Product, User

csrf = CSRFProtect(app)

with app.app_context():
    db.create_all()

    # db.session.add(User('admin','admin@gmail.com','admin',True))
    # db.session.add(User('BBW','BBW@gmail.com','BBW'))
    # db.session.commit()




UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# Initialiser Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Nom de la route de connexion

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/add', methods=['GET', 'POST'])
def add():
  form = ProductForm()
  if request.method == 'POST' and form.validate_on_submit():    
    libelle = form.libelle.data
    prix = form.prix.data
    description = form.description.data
    img = form.img.data

    print(form)

    file = secure_filename(img.filename)
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
    img_path = f'/static/uploads/{file}'

    prod = Product(libelle,prix,img_path, description)
    db.session.add(prod)
    db.session.commit()
    flash('Produit ajouté avec succès', 'success')
    return redirect(url_for('index'))
  return render_template('add.html', form=form)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = UserForm()
  if request.method == 'POST' and form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    user = User.query.filter_by(email=username, password=password).first()
    if user:
      login_user(user)
      return redirect(url_for('index'))
    
  return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))



@app.route('/')
@login_required
def index():
  search= request.args.get('search')
  products = Product.query.all()
  if search:
    results = [product for product in products if search.lower() in product.title.lower()]
    return render_template ('index.html', products=results)
  return render_template ('index.html', products=products)



@app.route('/detail/<int:id>', methods=['POST', 'GET'])
def detail(id):
  products = Product.query.all()
  for product in products:
    if product.id == id:
      return render_template ('detail.html', product=product)

@app.route('/panier')
def panier():
      panier = session.get('panier', [])
      products =[]
      for id in panier:
          product = Product.query.get(id)
          if product:
              products.append(product)
      total = sum(product.prix for product in products)
      return render_template ('panier.html', panier=products, total=total)

@app.route('/add_to_panier/<int:id>')
@login_required
def add_to_panier(id):
      if 'panier' not in session:
          session['panier'] = []
      panier = session['panier']
      if id not in panier:
          product = Product.query.get(id)
          if product:
            panier.append(id)
      session.modified = True
      return redirect(url_for('panier'))


@app.route('/vider_panier')
def vider_panier():
    panier = session.get('panier', [])
    if panier:
        panier.clear()
        session['panier'] = panier
        session.modified = True
    return redirect(url_for('index'))

@app.route('/sup_prodPanier/<int:id>')
def sup_prodpanier(id):
    panier = session.get('panier', [])
    if id in panier:
        panier.remove(id)
        session['panier'] = panier
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/pricing')
def pricing():
    return render_template ('pricing.html')
