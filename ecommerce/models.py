from ecommerce import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False, unique=True)
    codigo_barras = db.Column(db.String(13), nullable=False, unique=True)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False, unique=True)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Item {self.nome}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.String(60), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False, default=5000)

    itens = db.relationship('Item', backref='dono_user', lazy=True)
