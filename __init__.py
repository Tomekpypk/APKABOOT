from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Konfiguracja dla bazy danych
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Konfiguracja dla folderu statycznego
app.static_folder = 'blog'

# Importowanie widoków i modeli po konfiguracji aplikacji
from blog import routes, models
