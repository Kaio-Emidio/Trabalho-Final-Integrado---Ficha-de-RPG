from app import db

class HabDeus(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_deus = db.Column(db.Integer,
                        db.ForeignKey('deus.id'),
                        nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    nivel = db.Column(db.Integer,
                      nullable=False)
    descricao = db.Column(db.Text,
                          nullable=False)

    deus = db.relationship('Deus',
                           back_populates='habilidades')