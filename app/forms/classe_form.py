from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.classe import Classe


class ClasseForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Informe o nome da classe.'),
            Length(max=65, message='O nome deve ter no máximo 65 caracteres.')
        ]
    )
    vida_inicial = IntegerField(
        'Vida inicial',
        validators=[
            DataRequired(message='Informe a vida inicial.'),
        ]
    )
    vida_por_nivel = IntegerField(
        'Vida por nível',
        validators=[
            DataRequired(message='Informe a vida por nível.'),
        ]
    )
    dado_de_vida = StringField(
        'Dado de vida',
        validators=[
            DataRequired(message='Informe o dado de vida.'),
            Length(max=3, message='O dado de vida deve ter no máximo 3 caracteres.')
        ]
    )
    submit = SubmitField('Salvar')

    def __init__(self, classe_id=None, *args, **kwargs):
        self.classe_id = classe_id
        super().__init__(*args, **kwargs)

    def validate_nome(self, nome):
        existente = Classe.query.filter(
            Classe.nome == nome.data.strip(),
            Classe.id != self.classe_id
        ).first()
        if existente:
            raise ValidationError('Já existe uma classe com esse nome.')