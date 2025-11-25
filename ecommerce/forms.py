from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email


class CadastroForm(FlaskForm):
    usuario = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha', validators=[DataRequired(), Length(min=6, max=20)])
    senha2 = PasswordField(label='Confirmar senha', validators=[DataRequired(), EqualTo('senha1')])
    submit = SubmitField(label='Cadastrar')
