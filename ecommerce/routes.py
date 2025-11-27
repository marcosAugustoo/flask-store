from ecommerce import app, db
from flask import render_template, redirect, url_for, flash, request
from ecommerce.models import Item, User
from ecommerce.forms import CadastroForm, LoginForm, CompraProdutoForm, VendaProdutoForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def page_home():
    return render_template("home.html")


@app.route('/produtos', methods=['GET', 'POST'])
@login_required
def page_produto():
    compra_form = CompraProdutoForm()

    # ----- POST: tentativa de compra -----
    if request.method == 'POST':
        compra_produto = request.form.get('compra_produto')
        produto_obj = Item.query.filter_by(nome=compra_produto).first()

        if produto_obj:
            if current_user.compra_disponivel(produto_obj):
                produto_obj.compra(current_user)
                flash(f'Compra efetuada de {produto_obj.nome} com sucesso!', category='success')
            else:
                flash(f'Você não possui saldo suficiente para comprar o produto {produto_obj.nome}', category='danger')
        else:
            flash('Produto não encontrado!', category='danger')

        return redirect(url_for('page_produto'))

    # ----- GET: exibição dos produtos -----
    itens = Item.query.filter_by(dono=None).all()
    dono_itens = Item.query.filter_by(dono=current_user.id)
    return render_template("product_page.html", itens=itens, compra_form=compra_form, dono_itens=dono_itens)



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


@app.route('/logout')
def page_logout():
    logout_user()
    flash('Você saiu do sistema com sucesso!', category='success')
    return redirect(url_for('page_home'))
