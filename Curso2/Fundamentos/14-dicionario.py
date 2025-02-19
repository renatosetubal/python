
import pprint

filmes = {
    "O Alto da compadecida": {
        "Ano":2000,
        "Nota": 9.5,
        "genero": "Comédia"
    },
    "Duck Talles": {
        "Ano":1984,
        "Nota": 9.5,
        "genero": "Desenho"
    },
    "007 Golden Eye": {
        "Ano":1997,
        "Nota": 8.5,
        "genero": "Ação"
    }
}

p=pprint.PrettyPrinter(indent=4)
p.pprint(filmes)
print(filmes["Duck Talles"])
#Buscar informação dentro de um dicionário aninhado
print(filmes["Duck Talles"]["Nota"])
#Adicionar um novo filme
filmes["Duck Talles"]["Ator"] = "Tio Patinhas"
print(filmes["Duck Talles"])
#Excluir um dicionario
del filmes["007 Golden Eye"]
p.pprint(filmes)