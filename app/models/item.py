from app import db

class Item(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    quantidade = db.Column(db.Integer,
                           nullable=False,
                           default=1)

    personagem = db.relationship('Personagem',
                                 back_populates='itens')