from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField , SubmitField
from wtforms.validators import Length

class ModalAtributosForm(FlaskForm):
    # Força
    valor_for = IntegerField("Valor Base")
    outro_bon_for = IntegerField("Outro Bônus")
    # Destreza
    valor_des = IntegerField("Valor Base")
    outro_bon_des = IntegerField("Outro Bônus")
    # Constituição
    valor_con = IntegerField("Valor Base")
    outro_bon_con = IntegerField("Outro Bônus")
    # Inteligência
    valor_int = IntegerField("Valor Base")
    outro_bon_int = IntegerField("Outro Bônus")
    # Sabedoria
    valor_sab = IntegerField("Valor Base")
    outro_bon_sab = IntegerField("Outro Bônus")
    # Carisma
    valor_car = IntegerField("Valor Base")
    outro_bon_car = IntegerField("Outro Bônus")

    submit = SubmitField("Salvar")