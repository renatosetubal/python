movie = ["The Holy Grail", "The Life of Brian", "The Meaning of Life", "Alf", "Batman"]

for m in movie:
    print(m)

for m in movie:
    if m == "Alf":
        print("Achei o Alf")
        break

for m in movie:
    if m == "Alf":
        continue
    print(m)

#Dando opção para o usuário interagir
total=0
movie=input("Digite o nome do filme: ")
qtd=int(input("Digite a quantidade de avaliações: "))

for i in range(qtd):
    nota=float(input("Digite a nota para o filme: "))
    total += nota
if nota > 0:
    avaliacao= total / qtd
else:
    avaliacao = 0
print(f"Média de avaliação do filme {movie} é: {avaliacao:.2f}")