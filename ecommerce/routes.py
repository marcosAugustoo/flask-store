from ecommerce import app, db
from flask import render_template, url_for, redirect, flash
from ecommerce.models import Item, User
from ecommerce.forms import CadastroForm


@app.route('/')
def home():
    return render_template("home.html", active_page='home')


@app.route('/produtos')
def product_page():
    items = Item.query.all()
    return render_template('product_page.html', items=items, active_page='produtos')


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario = User(
            usuario=form.usuario.data,
            email=form.email.data,
            senha=form.senha1.data
        )

        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('page_cadastro'))

    if form.errors != {}:
        for err_list in form.errors.values():
            for err in err_list:
                flash(f'Erro ao cadastrar usuário: {err}')

    return render_template('cadastro.html', form=form)
