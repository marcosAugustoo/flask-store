from os import urandom

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação
app = Flask(__name__)

# Configs
app.config['SECRET_KEY'] = '5c11802192033b2de5e700f23183cea2b69a6c87cd43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)


def format_currency(value):
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


app.jinja_env.filters['currency'] = format_currency

# Importa rotas e modelos (depois de criar app e db)
from ecommerce import routes
from ecommerce import models
