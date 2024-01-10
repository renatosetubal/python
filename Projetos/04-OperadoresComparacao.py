x = y = z = False

print("Digite o número:")
n1 = int(input())
n2 = int(input('Digite o segundo número:'))

#Verificar se são iguais os números digitados
x = n1 == n2 
print('São iguais?', x, '\n') #\n equivale a dar um enter,  é uma quebra de linha1
#Verificandos se o primeiro numero é maior que o segundo
z = n1 > n2
print(n1, 'é maior que', n2, '?', z, '\n')
y = n1 != n2
print('São diferentes?' + str(y))