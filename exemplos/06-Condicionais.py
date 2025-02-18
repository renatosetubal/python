#Declarando as variáveis a serem utilizadas
n1 = n2 = media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Calculando a media de acordo com o que foi digitado pelo usuário
media = (n1 + n2) /2

##Condicional simples
if (media >= 7):
    #print("Sua média8 é: " + str(media) + " . Você foi aprovado! Parabéns!")
    print('Sua média é {}'.format(media) + ' Parabéns, você foi aprovado! ')

#####################Condicional composta 01
if (media >=7):
    print('Parabéns, você foi aprovado!')
    status = 'Aprovado'
else:
    if(media >= 0) and (media < 6):
        print('Lamentamos, você foi Reprovado!')
        status = 'Reprovado'
    else:
        if(media >=6) and (media < 7):
            print('Atenção, você está de recuperação!')
            status = 'Recuperação'

#####################Condicional composta 02 com uso do elif

if (media >=7):
    print('Parabéns, você foi aprovado!')
    status = 'Aprovado'
elif (media >= 6):
    print('Atenção, você está de recuperação!')
    status = 'Recuperação'
else:
    print('Lamentamos, você foi reprovado!')
    status = 'Reprovado'

print('Sua média foi {}'.format(media) + '. Você está {}'.format(status))
