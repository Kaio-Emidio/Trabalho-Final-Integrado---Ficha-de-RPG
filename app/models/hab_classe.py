from app import db

class HabClasse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_classe = db.Column(db.Integer,
                          db.ForeignKey('classe.id'),
                          nullable=False)
    nome = db.Column(db.String(65))
    nivel = db.Column(db.Integer)
    descricao = db.Column(db.Text)

    classe = db.relationship('Classe',
                             back_populates='habilidades')