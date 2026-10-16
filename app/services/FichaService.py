from app.models import Personagem
from app import db 

class FichaService:
    def salvar(ficha):
        try:
            ficha = Personagem()
            formulario.populate_obj(ficha)
            db.session.add(ficha)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Erro ao salvar ficha: {e}")
            db.session.rollback()
            return False
    
    def ler_informacoes(id):
        return db.session.get(Personagem, id)
    
    def buscar_por_id(id):
        query = db.select(Personagem).where(Personagem.id == id)
        return db.session.scalar(query)
    
    def atualizar(ficha, formulario):
        try:
            formulario.populate_obj(ficha)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar ficha: {e}")
            db.session.rollback()
            return False
            
    def remover(ficha):
        if ficha:
            db.session.delete(ficha)
            db.session.commit()
            return True
        else:
            db.session.rollback()
            return False