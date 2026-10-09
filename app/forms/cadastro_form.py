from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo
from app.services.UsuarioService import UsuarioService

class CadastroForm(FlaskForm):
    username = StringField('Usuário', 
                           validators=[
                               DataRequired(message='Por favor, preencha o nome do usuário')])
    email = EmailField('Email', 
                       validators=[
                           DataRequired(message='Por favor, preencha o email'), 
                           Email(message="Email inválido")])
    password = PasswordField('Senha', 
                             validators=[
                                 DataRequired(message='Por favor, preencha a senha'), 
                                 Length(
                                     min=5, 
                                     message="A senha deve contar mais de cinco caracteres")])
    password_conf = PasswordField('Confirmar senha', 
                                  validators=[
                                      DataRequired('Por favor, confirme sua senha'), 
                                      EqualTo('password', message="As senhas não coincidem")])
    
    submit = SubmitField('Salvar')

    def validate_username(self, username):
        if username.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')

    # def validate_username(self, username):
    #     if not UsuarioService.checar_unicidade(username.data.strip(), 'username'):
    #         raise ValidationError('Nome de usuário já cadastrado.')

    # def validate_email(self, email):
    #     if not UsuarioService.checar_unicidade(email.data.strip().lower(), 'email'):
    #         raise ValidationError('Email já cadastrado.')