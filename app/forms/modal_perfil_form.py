from flask_wtf import FlaskForm
from wtforms import StringField, SelectField , SubmitField
from wtforms.validators import Length

class ModalPerfilForm(FlaskForm):
    nome = StringField("Nome",
                       validators=[
                           Length(
                            max=65, 
                            message="O nome não pode ter mais de 65 caracteres")])
    alcunha = StringField("Alcunha",
                          validators=[
                              Length(
                                  max=65, 
                                  message="A alcunha não pode ter mais de 65 caracteres")])
    classe = SelectField("Classe",
                          choices=[
                              'Atacante',
                              'Conjurador',
                              'Tanque'])
    deus = SelectField("Deus",
                        choices=[
                              'Anúbis',
                              'Poseidon',
                              'Amaterasu'])
    raca = SelectField("Raça",
                        choices=[
                              'Humano',
                              'Elfo',
                              'Anão'])
    oficio = SelectField("Ofício",
                          choices=[
                                'Ferreiro',
                                'Alquimista',
                                'Caçador'])
    alinhamento = SelectField("Alinhamento",
                              choices=[
                                    'Leal e Bom',
                                    'Neutro e Bom',
                                    'Caótico e Bom',
                                    'Leal e Neutro',
                                    'Neutro',
                                    'Caótico e Neutro',
                                    'Leal e Mau',
                                    'Neutro e Mau',
                                    'Caótico e Mau'])
    jogador = StringField("Jogador")
    submit = SubmitField("Salvar")