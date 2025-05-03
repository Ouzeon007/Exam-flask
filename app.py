import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'une_clé_secrète_très_sécurisée'  # Changez ceci en production

import application.routes  

if __name__ == '__main__':
  app.run(debug=True)

