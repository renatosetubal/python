nome = "Renato"
letra = nome[2] #armazena letra na posição 2

print(len(nome)) #Verificando tamanho da string

#Concatenação
a = "Renato"
b = "Setubal"
print(a + " "+ b)

#Imprimir parte de uma string
print(nome[1:3])

#Manipultando e-mail e separando nome do dominio
#email = input('Digite o seu endereço de e-mail: ')
email = 'renato.setubal@gmail.com'
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

#Verificar se está contido em uma string
produtos = "Carbonato de sódio e óxido de zinco"
print('sódio' in produtos)
print('sódioa' not in produtos)

#Verificando em que posição aparece inicia uma string
item = 'banana caramelizada'
pos = item.find('car')
print(pos)
pos=item.find('flu')
print(pos) #retorna -1 caso não encontre. 
#Maiusculo e minusculo
celeste = 'galáxia esPiral M31'
print(celeste)
#Tudo em maiusculo
print(celeste.upper())
#tudo em minusculo
print(celeste.lower())
#capítalizar, primeira letra da frase em maiuscula
print(celeste.capitalize())
#Cada letra de cada palavra em maiusculo
print(celeste.title())

#Substituindo string
suplemento = 'Deka'
suplemento2 = suplemento.replace('Deka', 'durateston')
print(suplemento+ " "+ suplemento2)

#Remover espaço em branco
frase = '    Minha frase com espaço no início e fim.   '
print(frase)
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())

#Alinhamento de texto para edição
fruta = 'Abacaxi'
print(fruta) #Sem alinhamento
print(fruta.rjust(30)) #espaço de 30 caracteres a direita
print(fruta.center(20,'*')) #Alinhado ao centro
print(fruta.ljust(20,'-')) #Alinhado ao centro

#Prefixo e Sufixos - Retorna true e false
p = "Renato Miranda Setúbal"
print(p.startswith('Re'))
print(p.endswith('op'))

#Docstrings - usado para documentar o código - Pode ser usado atribuindo a variável também. 
texto = """
Dosctring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python, entre outros locais
Ela respeita o deslocamento do texto e é muito útil
"""
print(texto)






