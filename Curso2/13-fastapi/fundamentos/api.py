from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"Mensagem": "Olá Mundo API"}