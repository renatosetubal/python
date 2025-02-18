
n = 1
qtd = 2
while (n <= qtd):
   # print(str(n) + "  ",end='')
    n = n +1


valor = None
while True:
    print('Digite um número. Para sair, digite x: ')
    valor = input()
    if (valor == 'x') or (valor == 'X'):
        break #finaliza o laço de repetição onde ela está inserida
    print(f'Este é o número digitado: {valor}')
print('Programa Finalizado!')
