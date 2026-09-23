from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

class UsuarioForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o nome do usuário')])
    email = EmailField('Email', validators=[DataRequired(message='Por favor, preencha o email'), Email(message="Email inválido")])
    passaword = PasswordField (validators=[DataRequired() ,Length(min=5, message="Coloque uma senha válida")])
    submit = SubmitField('Salvar')