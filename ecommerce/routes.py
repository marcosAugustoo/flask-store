from ecommerce import app
from flask import render_template
from ecommerce.models import Item
from ecommerce.forms import CadastroForm


@app.route('/')
def home():
    return render_template("home.html", active_page='home')


@app.route('/produtos')
def product_page():
    items = Item.query.all()
    return render_template('product_page.html', items=items, active_page='produtos')


@app.route('/cadastro')
def page_cadastro():
    form = CadastroForm()
    return render_template('cadastro.html', form=form)
