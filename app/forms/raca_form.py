from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.raca import Raca


class RacaForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Informe o nome da raça.'),
            Length(max=65, message='O nome deve ter no máximo 65 caracteres.')
        ]
    )
    tipo_criatura = StringField(
        'Tipo de criatura',
        validators=[
            DataRequired(message='Informe o tipo de criatura.'),
            Length(max=65, message='O tipo deve ter no máximo 65 caracteres.')
        ]
    )
    tamanho = StringField(
        'Tamanho',
        validators=[
            DataRequired(message='Informe o tamanho.'),
            Length(max=65, message='O tamanho deve ter no máximo 65 caracteres.')
        ]
    )
    submit = SubmitField('Salvar')

    def __init__(self, raca_id=None, *args, **kwargs):
        self.raca_id = raca_id
        super().__init__(*args, **kwargs)

    def validate_nome(self, nome):
        existente = Raca.query.filter(
            Raca.nome == nome.data.strip(),
            Raca.id != self.raca_id
        ).first()
        if existente:
            raise ValidationError('Já existe uma raça com esse nome.')