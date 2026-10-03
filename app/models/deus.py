from app import db

class Deus(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False,
                     unique=True)

    habilidades = db.relationship('HabDeus',
                                  back_populates='deus')
    personagens = db.relationship('Personagem',
                                  back_populates='deus')