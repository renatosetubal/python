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

# Atualiza um jogador
@jogador_router.put("/jogadores/{jogador_id}")
async def atualiza_jogador(jogador_id, jogador: Jogador):
    #Caputar informações baseadas em id
    conn.local.jogador.find_one_and_update(
        {
            "_id":ObjectId(jogador_id)
        },
        {
            "$set": dict(jogador)
        }
    )
    return jogadorEntidade(
        conn.local.jogador.find_one({
            "_id":ObjectId(jogador_id)
        })
    )
# Excluir jogadores
@jogador_router.delete('/jogadores/{jogador_id}')
async def deleta_jogador(jogador_id, jogador: Jogador):
    return jogadorEntidade(
        conn.local.jogador.find_one_and_delete(
            {
                "_id":ObjectId(jogador_id)
            }
        )
    )
