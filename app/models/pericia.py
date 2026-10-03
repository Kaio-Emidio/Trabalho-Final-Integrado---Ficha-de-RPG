from app import db

class Pericia(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_atributo = db.Column(db.Integer,
                            db.ForeignKey('atributo.id'),
                            nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False,
                     unique=True)

    atributo = db.relationship('Atributo',
                               cascade='all, delete-orphan',
                               back_populates='pericias')
    