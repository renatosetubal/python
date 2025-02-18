#Sintaxe:
#for item in sequencia:

lista = [2,30,30,40,50]
palavra = "Renato"

for i in palavra:
    print(i)

#Exibindo sequencia de números através da função range. 
for numero in range(1,61):
    print(numero)

#RAnge tem tres paramentros - Valor inicial, valor final, incremento.    
for x in range(1,20,2):
    print(x)
#For usando sequência tupla
pedras = ('Rubi','Diamante','Safira','Jade','Esmeralda')
for pedra in pedras:
    if pedra == 'Diamante': #Vai imprimir todas as pedras da lista exceto o quartzo. Ele não encerra o laço apenas pula a pedra. 
        continue
    print(pedra)




