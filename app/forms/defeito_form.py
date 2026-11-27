from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.defeito import Defeito
from app.models.personagem import Personagem


class DefeitoForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Informe o nome do defeito.'),
            Length(max=65, message='O nome deve ter no máximo 65 caracteres.')
        ]
    )
    descricao = TextAreaField(
        'Descrição',
        validators=[DataRequired(message='Informe a descrição do defeito.')]
    )
    personagens = SelectField(
        'Personagem',
        coerce=int,
        validators=[DataRequired(message='Selecione o personagem.')]
    )
    submit = SubmitField('Salvar')

    def __init__(self, defeito_id=None, *args, **kwargs):
        self.defeito_id = defeito_id
        super().__init__(*args, **kwargs)
        self.personagens.choices = [
            (personagem.id, personagem.nome)
            for personagem in Personagem.query.order_by(Personagem.nome).all()
        ]

    def validate_nome(self, nome):
        existente = Defeito.query.filter(
            Defeito.nome == nome.data.strip(),
            Defeito.id != self.defeito_id
        ).first()
        if existente:
            raise ValidationError('Já existe um defeito com esse nome.')
