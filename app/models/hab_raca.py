from app import db

class HabRaca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_raca = db.Column(db.Integer,
                        db.ForeignKey('raca.id'),
                        nullable=False)
    nome = db.Column(db.String(65),
                     nullable=False)
    descricao = db.Column(db.Text,
                          nullable=False)

    raca = db.relationship('Raca',
                           back_populates='habilidades')