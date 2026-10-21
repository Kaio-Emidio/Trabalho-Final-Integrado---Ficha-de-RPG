from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired(message="Por Favor, preencha o nome de usuário")])
    password = PasswordField('Senha', validators=[DataRequired(message='Por favor, coloque uma senha válida'), Length(min=5, message="Coloque uma senha válida")])    
    remember_me = BooleanField("Continuar Logado") 
    submit = SubmitField('Entrar')
    