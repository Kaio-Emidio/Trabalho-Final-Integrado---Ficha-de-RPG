from app import db

class Ferramentas_e_Habilidades(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_personagem = db.Column(db.Integer,
                              db.ForeignKey('personagem.id'),
                              nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    proeficiente = db.Column(db.Boolean,
                             nullable=False)
    valor = db.Column(db.Integer,
                      nullable=False)
    
    personagens = db.relationship('Personagem',
                                  back_populates='ferramentas_e_habilidades')