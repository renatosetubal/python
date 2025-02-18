
#Codigo exemplo uso do AND
idade = 43
peso = 90
faixa = 'Roxa'

resultado = (idade >= 43) and (peso >= 89) and (peso <= 94) and (faixa == 'Roxa')

#Codigo para uso do OR
porta = 'a'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado ? ' + str(alarme)
print(msg)

#Codigo de exemplo uso do NOT
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' +  str(tem_dinheiro)
print(msg)