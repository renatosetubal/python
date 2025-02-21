from collections import Counter, namedtuple, deque
from operator import itemgetter

#1 - lista de frutas (contagem)
frutas = ['Maça', 'Banana',"Pêra","Uva","Maçã","Morango","Pêra","Pêra","Pêra","Morango","Goiaba"]
print(frutas)
print(Counter(frutas))

#2 - Utilizando tupla nomeada 
game = namedtuple('game',['name','price','note'])
g1 = game('Fifa 25',90.50,8.5)
g2 = game('NBA 2k',100.00, 10.0)
print(g1)
print(g2)

#3-Ordenar dicionários
e = {"Pedro":23,"Pedro":23,"Perla":33, "Ana":24, "Martha":50, }
ret= sorted(e.items(),key= itemgetter(0))
print(ret)
ret= sorted(e.items(),key= itemgetter(1))
print(ret)
#4 - Utilziando uma fila em ambas as extremidades

deq = deque([20,30,40,60,80])
deq.appendleft(22) #Adicionando a esquerda da fila
print(deq)
deq.append(78)
print(deq)
