from app import db

class Atributo(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    nome = db.Column(db.String(65),
                     nullable=False,
                     unique=True)

    personagens = db.relationship('Personagem_Atributo',
                                  cascade='all, delete-orphan',
                                  back_populates='atributo')
    pericias = db.relationship('Pericia',
                               back_populates='atributo')