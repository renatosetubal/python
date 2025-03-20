from fastapi import FastAPI
from routes.jogador_route import *

app = FastAPI()

app.include_router(jogador_router)