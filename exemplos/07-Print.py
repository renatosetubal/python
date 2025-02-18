#Sintaxe do comando
#print(objeto, argumentos)

#Exemplo 1
mensagem = "Exibindo a função de print"
print(mensagem)
print('Aula de python, teste de print')

#Exemplo 3
nome = "Renato Setúbal"
tecnologia = "Linux"
print('Tecnologia:',tecnologia, 'Lpic 2 -', nome)
#Exemplo 4 - Concatenando
# nome2 = input("Digite o seu nome: ")
# print('Olá ' + nome2 + " seja bem vindo!" ) #Por padrão o print coloca uma quebra de linha. 

#Exemplo 04 Imprimindo e permanecendo na mesma linha
print('Renato ', end='')
print('Miranda ', end='')
print('Setúbal')

#Exemplo 5 - usando o format para atribuir as variáveis no texto
nome3 = "Renato"
idade = "43"
msg_formatada = 'O nome dele é {0} e ela tem {1} anos'.format(nome3,idade)

#Exemplo 6 - usando o f string
nome4 = "Renato"
peso = "98"
mensagem = f'Olá, meu nome é {nome} e meu peso é {peso}'
print(mensagem)
#Exemplo 7 formatando um valor flutuante
valor = 130.05659
print(f'O valor é {valor:.2f}')

#Exemplo 8 caracteres de escape
valor2=30.56
print(f'O valor é \'{valor:.2f}\'') #Exibirá o valor entre aspas

#Exempolo 9 Executando em tabulação
name = "Maria"
idade = "12"
print(f'Nome:\t{name}\tIdade {idade}')
print(f'Nome: {name}\tIdade: {idade}')