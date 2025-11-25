from ecommerce import app, db, bcrypt
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
        senha_hash = bcrypt.generate_password_hash(form.senha1.data).decode('utf-8')

        usuario = User(
            usuario=form.usuario.data,
            email=form.email.data,
            senha=senha_hash
        )

        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('page_cadastro'))

    if form.errors:
        for err_list in form.errors.values():
            for err in err_list:
                flash(f'Erro ao cadastrar usuário: {err}', category='danger')

    return render_template('cadastro.html', form=form)
