###################Funções por posição e por parâmetro
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f'{modelo}, {ano}, {placa} - {marca}, {motor}, {combustivel}')

#Chamando a função
criar_carro("Hibrido", "2024", "ABD-56Y9", marca="Hyundai", motor="180cc", combustivel="gasolina")

###################Exemplo de função que obriga que seja passado por chaves

def cria_pessoa(*,nome, idade, estado_civil, sexo):
    print(f'{nome} {idade} {estado_civil} {sexo}')
#Neste caso é obrigatório usar keyword para passar os parâmetros
cria_pessoa(nome="Renato",idade="42",estado_civil="Casado",sexo="Masculino")

###################Usando de forma ao estado_civil ser usado como key ou como passo
def cria_pessoa2(nome, idade, /, estado_civil, *,sexo):
    print(f'{nome} {idade} {estado_civil} {sexo}')

cria_pessoa2("Renato","42","Casado", sexo="Masculino")
cria_pessoa2("Renato","43",estado_civil="Casado",sexo="Masculino")

##################Função e objeto de primeira classe. 
def  somar(a,b):
    return a + b,

def subratir(a,b):
    return a - b
#definindo nova função  com parâmetros incluindo uma função
def mostra_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'Este é o resultado do cálculo é: {resultado}')
    
mostra_resultado(20,10,somar)
mostra_resultado(20,10,subratir)