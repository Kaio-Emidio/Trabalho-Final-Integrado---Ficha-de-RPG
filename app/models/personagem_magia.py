from app import db

class Personagem_Magia(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    id_magia = db.Column(db.Integer,
                         db.ForeignKey('magia.id'),
                         nullable=False)
    preparada = db.Column(db.Boolean,
                          nullable=False,
                          default=False)

    personagem = db.relationship('Personagem',
                                  back_populates='magias')
    magia = db.relationship('Magia',
                            back_populates='personagens')