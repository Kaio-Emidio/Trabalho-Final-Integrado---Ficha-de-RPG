from app import db

class Idiomas_e_Outros(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    tipo = db.Column(db.Enum('Idioma',
                             'Arma',
                             'Armadura',
                             'Outro'),
                             name='tipo_enum')
    nome = db.Column(db.String(65))

    personagens = db.relationship('Personagem',
                                  back_populates='idiomas_e_outros')