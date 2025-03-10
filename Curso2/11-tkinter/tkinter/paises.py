from random import *

# Dicionário de países
paises = {
    "AR": "Argentina",
    "AU": "Austrália",
    "BE": "Bélgica",
    "BR": "Brasil",
    "CA": "Canadá",
    "CH": "Suiça",
    "CL": "Chile",
    "CM": "Camarões",
    "CN": "China",
    "CO": "Colômbia",
    "DE": "Alemanha",
    "EG": "Egito",
    "ES": "Espanha",
    "FR": "França"
}

paises_simbolo = []

for i in paises.keys():
    paises_simbolo.append(i.lower())
    
print(paises_simbolo)

def dados_pais():
    index_aleatorio = randrange(0, len(paises_simbolo))
    imagem = "img/{}.{}".format(paises_simbolo[index_aleatorio], "png")
    key = paises_simbolo[index_aleatorio].upper()
    pais_nome = paises[key]
    
    return [imagem, pais_nome]