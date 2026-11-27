from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class HabRacaForm(FlaskForm):
    id_raca = SelectField(
        'Raça',
        coerce=int,
        validators=[DataRequired(message='Selecione uma raça.')]
    )
    nome = StringField(
        'Nome',
        validators=[
            DataRequired(message='Informe o nome da habilidade.'),
            Length(max=65, message='O nome deve ter no máximo 65 caracteres.')
        ]
    )
    descricao = TextAreaField(
        'Descrição',
        validators=[DataRequired(message='Informe a descrição da habilidade.')]
    )
    raca = StringField(
        'Raça',
        validators=[
            DataRequired(message='Informe a raça da habilidade.'),
            Length(max=65, message='A raça deve ter no máximo 65 caracteres.')
        ]
    )
    
    submit = SubmitField('Salvar')
