listaNumeros=[i for i in range(10) if i <4]
print(listaNumeros)

lmovie=["The Holy Grail", "The Life of Brian", "The Meaning of Life", "Alf", "Batman"]
movieWithE=[m for m in lmovie if "e" in m.lower()]
print(movieWithE)

#Filmes já assistidos
filmeVisto=[m for m in lmovie if m != "Batman"]
print(filmeVisto)

#Encontrar Filme pelo nome
while True:
    busca= input("Digite o nome do filme ou digite 'sair' para encerrar: ")
    if busca.lower() == "sair":
        print("Saindo do programa")
        break
    encontrarFilme = [m for m in lmovie if busca.lower() in m.lower()]
    if encontrarFilme:
        print(f"Filme encontrado com o nome: {busca}: ")
        for movie in encontrarFilme:
            print(movie)
    else:
        print("Nenhum filme com o nome {movie} foi encontrado. Tente novamente!")