
try:
    letras=['a','b','c']
    print(letras[3])
except IndexError:
    print('Índice inexistente')

try:
    valor = int(input('Digite o valor do produto: '))
    print(valor)
except ValueError:
    print("Favor digitar um valor em número inteiro")
# else:
#     print('O valor digitado foi correto.')
#     print(valor *10)
finally:
    print('Codigo será executado de qualquer jeito, com ou sem erro')    