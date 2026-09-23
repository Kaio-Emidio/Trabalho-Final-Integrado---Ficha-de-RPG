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