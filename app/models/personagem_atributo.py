from app import db

class Personagem_Atributo(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    id_atributo = db.Column(db.Integer,
                            db.ForeignKey('atributo.id'),
                            nullable=False)
    valor = db.Column(db.Integer,
                      nullable=False,
                      default=10)
    proficiencia_salvaguarda = db.Column(db.Boolean,
                                         nullable=False,
                                         default=False)

    personagem = db.relationship('Personagem',
                                 back_populates='atributos')
    atributo = db.relationship('Atributo',
                               back_populates='personagens')