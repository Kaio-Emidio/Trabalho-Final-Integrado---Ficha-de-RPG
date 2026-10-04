from app import db

class Personagem(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    id_usuario = db.Column(db.Integer,
                           db.ForeignKey('usuario.id'),
                           nullable=False)
    id_classe = db.Column(db.Integer,
                          db.ForeignKey('classe.id'))
    id_raca = db.Column(db.Integer,
                        db.ForeignKey('raca.id'))
    id_deus = db.Column(db.Integer,
                        db.ForeignKey('deus.id'))
    id_oficio = db.Column(db.Integer,
                          db.ForeignKey('oficio.id'))
    id_alinhamento = db.Column(db.Integer,
                               db.ForeignKey('alinhamento.id'),
                               nullable=False)
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
    genero = db.Column(db.String(65))
    cabelo = db.Column(db.String(65))
    olho = db.Column(db.String(65))
    pele = db.Column(db.String(65))
    aura = db.Column(db.String(65))
    roupas = db.Column(db.Text)
    tracos_personalidade = db.Column(db.Text)
    ideais = db.Column(db.Text)
    ligacoes = db.Column(db.Text)
    defeitos = db.Column(db.Text)
    dinheiro = db.Column(db.Int)

    jogador = db.relationship('Usuario',
                              back_populates='personagens')
    classe = db.relationship('Classe',
                             back_populates='personagens')
    raca = db.relationship('Raca',
                           back_populates='personagens')
    deus = db.relationship('Deus',
                           back_populates='personagens')
    oficio = db.relationship('Oficio',
                             back_populates='personagens')
    alinhamento = db.relationship('Alinhamento',
                                   back_populates='personagens')
    atributos = db.relationship('Personagem_Atributo',
                                cascade='all, delete-orphan',
                                back_populates='personagem')
    pericias = db.relationship('Personagem_Pericia',
                               cascade='all, delete-orphan',
                               back_populates='personagem')
    ferramentas_e_habilidades = db.relationship('Ferramentas_e_Habilidades',
                                                back_populates='personagens')
    magias = db.relationship('Personagem_Magia',
                             cascade='all, delete-orphan',
                             back_populates='personagem')
    idiomas_e_outros = db.relationship('Idiomas_e_Outros',
                                        back_populates='personagens')
    talentos = db.relationship('Talento',
                               back_populates='personagem')
    defeitos = db.relationship('Defeito',
                               back_populates='personagem')
