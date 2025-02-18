import random

valor = random.randint(1,60)
print(valor)

valor_float = random.random()
print(f'Número gerado com duas casas decimais: {round(valor_float * 10, 2)}')


#Gerar número de 1 a 100 com ponto flutuante
valor = random.uniform(1,100)
print(f'Número: {round(valor, 2)}') #Ajustando o valor das casas decimais uma vez que gerará float

#Pegando o valor aleatório de uma lita
lista = [2,5,7,8,9,12,14,15,17,29,30,33]
valor = random.choice(lista)
print(f'Número escolhido: {valor}')

#Pegar vários valores desta lista
lista = range(1,60 ) #Definindo os itens da lista, no caso de 1 a 60
valor = random.sample(lista,6) #Pega seis numeros desta lista
print(f'Número escolhido: {valor}') #Exibe os valores

#Embaralhar elementos da sequência
lista = list(range(1,60)) #Definindo os itens da lista, no caso de 1 a 60
emb = random.shuffle(lista)
print(f'Valores embaralhados: {lista}')