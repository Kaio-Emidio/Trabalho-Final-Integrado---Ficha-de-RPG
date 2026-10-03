from app import db

class Raca(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False,
                     unique=True)
    tipo_criatura = db.Column(db.String(65),
                              nullable=False)
    tamanho = db.Column(db.String(65),
                        nullable=False)

    habilidades = db.relationship('HabRaca',
                                  back_populates='raca')
    personagens = db.relationship('Personagem',
                                  back_populates='raca')