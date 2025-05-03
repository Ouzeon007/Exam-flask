# Application E-Commerce Flask

## Description du Projet

Cette application web est une plateforme e-commerce développée avec Flask permettant aux utilisateurs de parcourir, rechercher et acheter des produits en ligne. Le projet a été conçu dans le cadre du cours de programmation à l'ISM.

## Fonctionnalités Principales

- **Authentification des utilisateurs** : Système de connexion et gestion des sessions
- **Catalogue de produits** : Affichage et recherche de produits
- **Détails des produits** : Page dédiée pour chaque produit avec description détaillée
- **Panier d'achat** : Ajout/suppression de produits et gestion du panier
- **Administration** : Interface d'administration pour la gestion des produits (ajout, modification)
- **Upload d'images** : Possibilité d'ajouter des images pour les produits

## Technologies Utilisées

- **Backend** : Flask (Python)
- **Base de données** : SQLite (via SQLAlchemy)
- **Frontend** : HTML, CSS (Tailwind CSS)
- **Authentification** : Flask-Login
- **Formulaires** : Flask-WTF
- **Migrations** : Flask-Migrate (Alembic)
- **Administration** : Flask-Admin

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel :
   ```
   python -m venv .venv
   ```
3. Activer l'environnement virtuel :
   - Windows : `.venv\Scripts\activate`
   - Linux/Mac : `source .venv/bin/activate`
4. Installer les dépendances :
   ```
   pip install -r requirement.txt
   ```
5. Initialiser la base de données :
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Exécution

Pour lancer l'application en mode développement :

```
python app.py
```

L'application sera accessible à l'adresse : http://localhost:5000

## Structure du Projet

```
├── app.py                  # Point d'entrée de l'application
├── database.py             # Configuration de la base de données
├── models.py               # Modèles de données (Product, User)
├── requirement.txt         # Liste des dépendances
├── application/            # Package principal de l'application
│   ├── __init__.py         # Initialisation du package
│   ├── forms.py            # Définition des formulaires
│   └── routes.py           # Définition des routes
├── db/                     # Dossier contenant la base de données SQLite
├── migrations/             # Fichiers de migration de la base de données
├── static/                 # Fichiers statiques
│   ├── css/                # Fichiers CSS (Tailwind)
│   └── uploads/            # Images uploadées
└── templates/              # Templates HTML
    ├── add.html            # Formulaire d'ajout de produit
    ├── detail.html         # Page de détail d'un produit
    ├── index.html          # Page d'accueil
    ├── layout.html         # Template de base
    ├── login.html          # Page de connexion
    └── panier.html         # Page du panier
```

## Fonctionnalités à Venir

- Système de paiement en ligne
- Gestion des stocks
- Système de notation et commentaires
- Historique des commandes
- Interface responsive pour mobile

## Auteur

Développé dans le cadre du cours de programmation à l'ISM.
