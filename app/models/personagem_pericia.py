from app import db

class Personagem_Pericia(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    id_pericia = db.Column(db.Integer,
                           db.ForeignKey('pericia.id'),
                           nullable=False)
    proficiencia = db.Column(db.Boolean,
                             nullable=False,
                             default=False)
    especializacao = db.Column(db.Boolean,
                                nullable=False,
                                default=False)
    bonus_outro = db.Column(db.Integer,
                            nullable=False,
                            default=0)

    personagem = db.relationship('Personagem',
                                 back_populates='pericias')
    pericia = db.relationship('Pericia',
                              back_populates='personagens')