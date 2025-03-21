from fastapi import FastAPI
from routes.jogador_route import *
from fastapi.middleware.cors import CORSMiddleware

client_app = [
    "http://localhost:3000"
]
app = FastAPI()

app.include_router(jogador_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=client_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)