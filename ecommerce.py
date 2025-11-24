from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando objeto
db = SQLAlchemy(app)


# Criando tabela
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=True)
    codigo_barras = db.Column(db.String(13), nullable=False, unique=True)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False, unique=True)


@app.route('/')
def home():
    return render_template('home.html', active_page='home')


@app.route('/produtos')
def product_page():
    items = Item.query.all()
    return render_template('product_page.html', items=items, active_page='produtos')


# Criando função de moeda
def format_currency(value):
    return f"R$ {value:.2f}".replace(',', 'X').replace(".", ',').replace('X', '.')


app.jinja_env.filters['currency'] = format_currency
