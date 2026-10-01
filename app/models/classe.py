from app import db

class Classe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(65))
    vida_inicial = db.Column(db.Integer)
    vida_por_nivel = db.Column(db.Integer)
    dado_de_vida = db.Column(db.String(3))

    personagens = db.relationship('Personagem',
                                  back_populates='classe')
    habilidades = db.relationship('HabClasse',
                                  back_populates='classe')