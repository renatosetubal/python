from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///meubanco.db', echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

#1 - Inserindo dadosde filmes
def add_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# add_filme('Matrix', 1999, 9.0)
# add_filme('O Poderoso Chefão', 1972, 9.2)       
# add_filme('O Senhor dos Anéis: O Retorno do Rei', 2003, 8.9)
# add_filme('Vingadores: Ultimato', 2019, 8.4)

def update_filme(id, nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
    session.commit()
    session.close()

# update_filme(1, 'Homem Aranha', 1973, 6.0)
def remove_filme(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()
remove_filme(1)