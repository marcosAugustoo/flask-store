from ecommerce import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(60), nullable=False)
    valor = db.Column(db.Integer, nullable=False, default=5000)

    itens = db.relationship('Item', backref='dono_user', lazy=True)

    @property
    def formataValor(self):
        if len(str(self.valor)) > 4:
            return f'R$ {self.valor:,}.00'
        else:
            return f'R$ {self.valor:,}'

    # Define senha criptografada
    def set_password(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode('utf-8')

    # Checa senha digitada
    def check_password(self, senha_texto):
        return bcrypt.check_password_hash(self.senha, senha_texto)

    def __repr__(self):
        return f"<User {self.usuario}>"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=True)
    preco = db.Column(db.Integer, nullable=False)
    cod_barra = db.Column(db.String(12), nullable=False, unique=True)
    descricao = db.Column(db.String(1024), nullable=False, unique=True)

    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item {self.nome}"
