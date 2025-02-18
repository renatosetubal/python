nome = 'Renato Setúbal' #String
nome_padrao = 'A variável não pooe começar com número' #String com nome composto
media = 1+2 #numero inteiro
media_dois = 1.0+3.2 #float
name, age = 'Renato Setubal',43 #multipla declaração com atribuição diferente
estado = True #Valores boleanos/lógico

#print(nome[1])
#print(media)
#print(name, age)

#Função type() -> vai retornar o tipo da variável. 
# print(type(media))
# print(type(name))
# print(type(estado))
# print(type(media_dois))

#Função isinstance() - é instancia -> retorna um valor verdadeiro ou falso se a variável for de um tipo. (boolean)

a=10.5
b='Nome'
print(isinstance(a,int)) #Verifica se é do tipo int
print(isinstance(a,(float, int))) #Verifica mais de um tipo