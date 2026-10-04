from app import db

class Oficio(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False)
    ferramentas = db.Column(db.String(65))
    descricao = db.Column(db.Text)

    personagens = db.relationship('Personagem',
                                  back_populates='oficio')