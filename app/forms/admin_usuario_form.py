from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

from app.models import Usuario


class AdminUsuarioForm(FlaskForm):
    username = StringField(
        'Usuário',
        validators=[
            DataRequired(message='Informe o nome do usuário.'),
            Length(max=65, message='O usuário deve ter no máximo 65 caracteres.')
        ]
    )
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='Informe o email.'),
            Email(message='Informe um email válido.'),
            Length(max=65, message='O email deve ter no máximo 65 caracteres.')
        ]
    )
    submit = SubmitField('Salvar alterações')

    def __init__(self, usuario_id, *args, **kwargs):
        self.usuario_id = usuario_id
        super().__init__(*args, **kwargs)

    def validate_username(self, username):
        existente = Usuario.query.filter(
            Usuario.username == username.data.strip(),
            Usuario.id != self.usuario_id
        ).first()
        if existente:
            raise ValidationError('Este nome de usuário já está cadastrado.')

    def validate_email(self, email):
        existente = Usuario.query.filter(
            Usuario.email == email.data.strip().lower(),
            Usuario.id != self.usuario_id
        ).first()
        if existente:
            raise ValidationError('Este email já está cadastrado.')
