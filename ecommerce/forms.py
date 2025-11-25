from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email, ValidationError

from ecommerce import bcrypt
from ecommerce.models import User


class CadastroForm(FlaskForm):
    usuario = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha', validators=[DataRequired(), Length(min=6, max=20)])
    senha2 = PasswordField(label='Confirmar senha', validators=[DataRequired(), EqualTo('senha1')])
    submit = SubmitField(label='Cadastrar')

    def validate_usuario(self, field):
        user = User.query.filter_by(usuario=field.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro usuário.")

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError("Email já existe! Cadastre outro email.")
