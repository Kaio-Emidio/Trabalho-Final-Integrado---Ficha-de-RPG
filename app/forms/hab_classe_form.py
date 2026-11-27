from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class HabClasseForm(FlaskForm):
    id_classe = SelectField(
        'Classe',
        coerce=int,
        validators=[DataRequired(message='Selecione uma classe.')]
    )
    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Informe o nome da habilidade.'),
            Length(max=65, message='O nome deve ter no máximo 65 caracteres.')
        ]
    )
    nivel = IntegerField(
        'Nível',
        validators=[
            DataRequired(message='Informe o nível da habilidade.'),
            NumberRange(min=1, message='O nível deve ser maior que zero.')
        ]
    )
    descricao = TextAreaField(
        'Descrição',
        validators=[DataRequired(message='Informe a descrição da habilidade.')]
    )
    submit = SubmitField('Salvar')
