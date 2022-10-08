from sql_alquemy import Base, engine, session
from sqlalchemy import Column, String, Integer

class ContatoLojaModel(Base):
    __tablename__ = 'contato_lojas'

    contato_loja_id = Column(Integer, primary_key=True)
    celular = Column(String(40))
    titular_celular = Column(String(40))
    telefone_fixo = Column (String(100))
    titular_telefone_fixo = Column(String(40))
    instagram = Column(String(100))
    facebook = Column(String(100))
    linkedin = Column(String(100))

    def __init__(self, celular,titular_celular, telefone_fixo, titular_telefone_fixo, instagram, facebook, linkedin):
        self.celular = celular
        self.titular_celular = titular_celular
        self.telefone_fixo = telefone_fixo
        self.titular_telefone_fixo = titular_telefone_fixo
        self.instagram = instagram
        self.facebook = facebook
        self.linkedin = linkedin
        
        
    
    def json(self):
        return {
            'contato_loja_id': self.contato_loja_id,
            'celular': self.celular,
            'titular_celular': self.titular_celular,
            'telefone_fixo': self.telefone_fixo,
            'titular_telefone_fixo': self.titular_telefone_fixo,
            'instagram': self.instagram,
            'facebook': self.facebook,
            'linkedin': self.linkedin
        }

    @classmethod
    def buscar_todos_contatos(cls):
        resultado = session.query(ContatoLojaModel).all()
        contatos = [contato.json() for contato in resultado]
        return contatos
    
    @classmethod
    def buscar_contato_por_id(cls, contato_loja_id):
        contato = session.query(ContatoLojaModel).filter_by(contato_loja_id=contato_loja_id).first()

        if contato:
            return contato
        return False

    def atualizar_contato(self, celular,titular_celular, telefone_fixo, titular_telefone_fixo, instagram, facebook, linkedin):
        self.celular = celular
        self.titular_celular = titular_celular
        self.telefone_fixo = telefone_fixo
        self.titular_telefone_fixo = titular_telefone_fixo
        self.instagram = instagram
        self.facebook = facebook
        self.linkedin = linkedin

    def salvar_contato(self):
        session.add(self)
        session.commit()

    def deletar_contato(self):

        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)