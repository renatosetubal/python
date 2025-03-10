from random import *

#Criando o dicionario de países

paises = {
    "AR": "Argentina",
    "AU": "Austrália",
    "BE": "Bélgica",
    "BR": "Brasil",
    "CA": "Canadá",
    "CH": "Suiça",
    "CL": "Chile",
    "CM": "Camarões", 
    "CN" : "China",
    "CO": "Colombia",
    "DE" : "Alemanha",
    "EG" : "Egito",
    "ES" : "Espanha",
    "FR" : "França"
}

paises_simbolos=[]
for i in paises.keys():
    paises_simbolos.append(i.lower())

def dados_pais():
    indice = randrange(0, len(paises_simbolos))
    imagem= "img/{}.{}".format(paises_simbolos[indice],"png")
    chave = paises_simbolos[indice].upper()
    pais_nome = paises[chave]
    return [imagem, pais_nome]
