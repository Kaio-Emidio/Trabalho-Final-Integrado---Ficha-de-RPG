from app import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(65),
                         index=True,
                         unique=True,
                         nullable=False)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(65),
                      index=True,
                      unique=True,
                      nullable=False)
    
    personagens = db.relationship('Personagem',
                                  back_populates='jogador')