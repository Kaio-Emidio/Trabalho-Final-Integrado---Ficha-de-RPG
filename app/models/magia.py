from app import db

class Magia(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False)
    escola = db.Column(db.String(65))
    circulo = db.Column(db.Integer,
                        nullable=False)
    tempo_de_conjuracao = db.Column(db.String(65))
    alcance = db.Column(db.String(65))
    componentes = db.Column(db.String(65))
    duracao = db.Column(db.String(65))
    descricao = db.Column(db.Text)

    personagens = db.relationship('Personagem_Magia',
                                  cascade='all, delete-orphan',
                                  back_populates='magia')