from app import db

class Contador(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    atual = db.Column(db.Integer,
                      nullable=False)
    maximo = db.Column(db.Integer,
                       nullable=False)

    personagem = db.relationship('Personagem',
                                 back_populates='contadores')