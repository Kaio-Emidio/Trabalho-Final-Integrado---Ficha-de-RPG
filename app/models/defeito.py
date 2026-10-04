from app import db

class Defeito(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    descricao = db.Column(db.Text,
                          nullable=False)

    personagens = db.relationship('Personagem',
                                  back_populates='defeitos')