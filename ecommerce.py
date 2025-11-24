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
    items = [
        {
            'id': 1,
            'name': 'Celular',
            'code_bar': '123451',
            'price': 2000
        },
        {
            'id': 2,
            'name': 'Notebook',
            'code_bar': '123452',
            'price': 3000
        },
        {
            'id': 3,
            'name': 'Tablet',
            'code_bar': '123453',
            'price': 1500
        },
        {
            'id': 4,
            'name': 'Mouse',
            'code_bar': '123454',
            'price': 500
        }
    ]
    return render_template('product_page.html', items=items, active_page='produtos')
