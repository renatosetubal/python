#Funções Básicas
def funcao01():
    print("Minha primeira função")

def funcao02(nome):
    print(f'Bem vindo {nome}!')
def funcao03(valor="Anônimous"):
    print(f'Seja bem vindo {valor}!')

funcao01()
funcao02("renato")
funcao02(nome="Jamal")
funcao03()
funcao03(valor='Manoel Gomes')

#Função com retornos none e multiplos (retorna tuplas)
def funcao04(nome, sobrenome):
    nomecompleto = (f'{nome} {sobrenome}')
    return nome, sobrenome, nomecompleto

print(funcao04("Renato","Miranda Setúbal"))

#Argumentos nomeados
def salva_carro(marca, modelo, ano, placa):
    print(f'Carro foi inserido com sucesso: {marca}/{modelo}/{ano}/{placa}')
#Forma recomendada é mapeando as variáveis logo nos parâmetros, assim evita problemas se a ordem for mudada.     
def salva_carro02(marca="Fiat", modelo="147", ano="1981", placa="ABC-34F5"):
    print(f'Carro foi inserido com sucesso: {marca}/{modelo}/{ano}/{placa}')

salva_carro('Mercedez','A4','2001',"ABC-45F9")
salva_carro02('BMW','X1','2023',"ABC-65F9")