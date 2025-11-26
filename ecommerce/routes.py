from ecommerce import app, db
from flask import render_template, redirect, url_for, flash
from ecommerce.models import Item, User
from ecommerce.forms import CadastroForm, LoginForm
from flask_login import login_user


@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos')
def page_produto():
    itens = Item.query.all()
    return render_template("product_page.html", itens=itens)


@app.route('/cadastro', methods=['GET', 'POST'])
def page_cadastro():
    form = CadastroForm()

    if form.validate_on_submit():
        usuario = User(
            usuario=form.usuario.data,
            email=form.email.data
        )

        # Criptografa a senha corretamente
        usuario.set_password(form.senha1.data)

        db.session.add(usuario)
        db.session.commit()

        flash("Cadastro realizado com sucesso!", category="success")
        return redirect(url_for('page_produto'))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário: {err}", category="danger")

    return render_template("cadastro.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form = LoginForm()

    if form.validate_on_submit():
        usuario_logado = User.query.filter_by(email=form.email.data).first()

        if usuario_logado and usuario_logado.check_password(form.senha.data):
            login_user(usuario_logado)
            flash(f'Sucesso! Você está logado como: {usuario_logado.usuario}', category='success')
            return redirect(url_for('page_produto'))
        else:
            flash('Email ou senha incorretos! Tente novamente.', category='danger')

    return render_template('login.html', form=form)
