from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogadorEntidade, listaJogadoresEntidade

jogador_router = APIRouter()

@jogador_router.get('/')
async def inicio():
    return "Bem vindo ao FullStack Farm"

# Lista todos os Jogadores
@jogador_router.get('/jogadores')
async def lista_jogadores():
    return listaJogadoresEntidade(conexao.farm1.jogador.find())

# Insere novos Jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.farm1.jogador.insert_one(dict(jogador))
    return listaJogadoresEntidade(conexao.farm1.jogador.find())