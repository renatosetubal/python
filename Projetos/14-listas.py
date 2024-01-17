#Lista: Representa uma sequência de valores armazenados em memória. 
#Sintaxe: nome_lista=[valores]
#As listas inicia-se em índice 0. 
notas = [5,9,6,3,7]
print(notas)

#concatenando duas listas de numeros
n1 = [2,5,6,7,8,98,8]
n2 = [1,3,9,10]
merge_lista = n1 + n2
print(merge_lista)

#Imprimindo a lista em um determincdo intervalo SLICE
print(merge_lista[0:5]) #Imprimirá os 5 primeiros números. 

#Verificando o tamanho da lista
print(len(merge_lista))

#trazer os valores da lista em ordem crescente
print(sorted(merge_lista))

#mostrar a ordem reversa ordenada
print(sorted(merge_lista,reverse=True))

#Somar todos os valores da lista
print(sum(merge_lista))

#Adicionando item a uma lista
merge_lista.append(354)
print(merge_lista)

#removendo item da lista, último item
merge_lista.pop()
print(merge_lista)

#Removento o item de acordo com a sua posição
merge_lista.pop(2) #removerá o 3 elemento da lista (A lista começa em 0)
print(merge_lista)

#Adcionando um item em uma determinada posição da lista (ele substituirá o item da lista caso ele exista)
merge_lista.insert(2,50)
print(merge_lista)

#Verificar se existe um número/ item na lista
print(50 in merge_lista) #Retorna true ou false

#Lista com laço for
planets = ['Mercúrio', 'Saturno', 'Netuno','Terra' ,'Venus'] #Criando lista vazia ou usar planetas = list()

for p in planets:
    print(f'{p}')



