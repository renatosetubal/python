#Trata se de um laço dentro de outro laço

#Exemplo com for

for i in range (1,6):
    print(f'\nRodada: {i}')
    for x in range(5,0,-1):
        print(f'Valor Interno :{x}')

import random

for a in range(1,6):
    print(f'\nConjunto {a}')
    for b in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')