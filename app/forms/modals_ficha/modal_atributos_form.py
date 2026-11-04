from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField , SubmitField

class ModalAtributosForm(FlaskForm):
    # Força
    valor_for = IntegerField("Valor Base")
    outro_bon_for = IntegerField("Outro Bônus")
    salv_prof_for = BooleanField("Proeficiente")
    outro_bon_salv_for = IntegerField("Outro Bonus")
    # Destreza
    valor_des = IntegerField("Valor Base")
    outro_bon_des = IntegerField("Outro Bônus")
    salv_prof_des = BooleanField("Proeficiente")
    outro_bon_salv_des = IntegerField("Outro Bonus")
    # Constituição
    valor_con = IntegerField("Valor Base")
    outro_bon_con = IntegerField("Outro Bônus")
    salv_prof_con = BooleanField("Proeficiente")
    outro_bon_salv_con = IntegerField("Outro Bonus")
    # Inteligência
    valor_int = IntegerField("Valor Base")
    outro_bon_int = IntegerField("Outro Bônus")
    salv_prof_int = BooleanField("Proeficiente")
    outro_bon_salv_int = IntegerField("Outro Bonus")
    # Sabedoria
    valor_sab = IntegerField("Valor Base")
    outro_bon_sab = IntegerField("Outro Bônus")
    salv_prof_sab = BooleanField("Proeficiente")
    outro_bon_salv_sab = IntegerField("Outro Bonus")
    # Carisma
    valor_car = IntegerField("Valor Base")
    outro_bon_car = IntegerField("Outro Bônus")
    salv_prof_car = BooleanField("Proeficiente")
    outro_bon_salv_car = IntegerField("Outro Bonus")

    submit = SubmitField("Salvar")