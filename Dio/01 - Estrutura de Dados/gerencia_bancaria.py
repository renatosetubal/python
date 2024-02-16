import os


lista_movimento = []
qtd_saque=0


class Movimento:
  def __init__(self, valor, tipo):
    self.valor = valor
    self.tipo = tipo

def deposito(mov):
    lista_movimento.append(mov)
    print(f'Foi depositado o valor de {mov.valor}. Confira no extrado, opção 3 do menu principal')
    input("Tecle enter para continuar...")
    

def saque(mov):
    global qtd_saque
    if mov.valor > 500:
        print(f'Valor excede limite diário.')
        input()
    elif qtd_saque > 2:
        print(f'Quantidade de saque diário excedido.')    
        input()
    else:
        total = busca_total()
        if mov.valor > total:
            print(f'Saldo insuficiente para saque! Saldo: {total}')
            input()
        else:
            lista_movimento.append(mov)            
            print(f'Foi retirado o valor de {mov.valor}. Confira a movimentação no menu 3')
            input("Tecle enter para continuar...")
            qtd_saque+=1

def extrato():
    valor=0.0
    for item in lista_movimento:

        print(f'Tipo Movimento: {item.tipo} - Valor R${item.valor}')
        if item.tipo == "Entrada":
            valor+=item.valor
        else:
            valor-=item.valor   
    print(f'==================Valor total R$ {valor}')  
    input()
    os.system('cls')

def busca_total():
    valor=0.0
    for item in lista_movimento:
        if item.tipo == "Entrada":
            valor+=item.valor
        else:
            valor-=item.valor  
    return valor

opcao=-1
menu=(f"""########MENU########
  1 - Depositar
  2 - Sacar
  3 - Exibir extrato
  0 - Sair
########BANK########""")

while opcao != 0:
    os.system('cls')
    print(menu)
    opcao=int(input("Digite a opção: "))
    if opcao == 1 :
       os.system('cls')
       valor=float(input('Digite o valor a ser depositado: '))
       deposito(Movimento(valor,"Entrada"))
    elif opcao == 2:
        os.system('cls')
        valor=float(input('Digite o valor a ser retirado: '))
        saque(Movimento(valor,"Saida"))
            
            
    elif opcao == 3:
       os.system('cls')
       extrato()   
