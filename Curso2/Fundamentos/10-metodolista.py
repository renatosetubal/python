filme =["Matrix","1999","9.3",True]
print(filme)
listaDeFilmes=["Matrix","Se beber não case", "Eu sei o eu você fez no verão passado",
               "O bebê de Rosemary", "O Exorcismo de Emilly Rose", "O Exorcista", "Madagascar"]
#Tamanho da lista
print(len(listaDeFilmes))
#Recuperar  o indice da lista pelo nome
print(listaDeFilmes.index("Madagascar"))
#Adicionar item ao final da lista
listaDeFilmes.append("Sexta feira 13")
print(listaDeFilmes)
#Ordenar a lista por nome
listaDeFilmes.sort()
print(listaDeFilmes)
#Copiar os itens de uma lista para outra
copialista=listaDeFilmes.copy()
print(copialista)
#Remover um item da lista
copialista.remove("O Exorcista")
print(copialista)
#Remover todos os itens da lista
copialista.clear()
print(copialista)
