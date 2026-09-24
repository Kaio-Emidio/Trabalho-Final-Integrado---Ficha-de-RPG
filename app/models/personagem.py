from app import db

class Personagem(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_usuario = db.Column(db.)
    id_classe = db.Column(db.)
    id_deus = db.Column(db.)
    id_raca = db.Column(db.)
    id_oficio = db.Column(db.)
    id_alinhamento = db.Column(db.)
    nome = db.Column(db.String(65))
    alcunha = db.Column(db.String(65))
    nivel = db.Column(db.Integer)
    conceito = db.Column(db.Text)
    vida_atual = db.Column(db.Integer)
    vida_temporaria = db.Column(db.Integer)
    mana_atual = db.Column(db.Integer)
    dados_vida = db.Column(db.Integer)
    meio_conjurador = db.Column(db.Boolean)
    idade = db.Column(db.Integer)
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    genero = db.Column(db.