from app import db

class Alinhamento(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False)

    personagens = db.relationship('Personagem',
                                  back_populates='alinhamento')