from fastapi import APIRouter
from config.database import conn
from models.jogador_model import Jogador
from schemas.jogador_schema import jogadorEntidade, listaJogadoresEntidade
from bson import ObjectId

jogador_router = APIRouter()

@jogador_router.get('/')
async def inicio():
    return "Bem vindo ao FullStack Farm"

# Lista todos os Jogadores
@jogador_router.get('/jogadores')
async def lista_jogadores():
    return listaJogadoresEntidade(conn.local.jogador.find())

#Detalhes de um Jogador
@jogador_router.get('/jogadores/{jogador_id}')
def busca_jogador_id(jogador_id):
    return jogadorEntidade(conn.local.jogador.find_one
        (
            {"_id":ObjectId(jogador_id)}
        )
    )


# Insere novos Jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conn.local.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conn.local.jogador.find())