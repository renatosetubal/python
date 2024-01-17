#Tuplas permite que voce tenha vários dados 
#Tuplas são imutáveis, o conteúdo não pode ser alterado depois de criadas
#Podem ter todos os tipos de dados. 
#Funciona como sequÊncia de constantes

tupla = (2,3,4,5,6,7)
print(tupla)

halogenios = ('F','Cl','I','At')
gases_nobres = ('He', 'Ne', 'Ar','Xe', 'Kr', 'Rn')
#imprimindo a tupla halogenios
print(halogenios)
#Imprimindo o tamanho da tupla de halogenios
print(len(halogenios))
#Imprimindo um dado em uma determianda posiçao da tupla
print(halogenios[1])
#Fazendo merge de duas tuplas
el = halogenios + gases_nobres
print(el)

#Contar quantidade de ocorrencia de numeros em uma tupla
t = (1,2,3,4,6,2,4,6,2,5,2,2,0)
print(t.count(2))
#fazendo slice na tupla
print(halogenios[0:2]) #Imprimindo do elemento 0 até o 2
print(halogenios[:3]) #Imprimindo do inicio até o elemento 3
print(halogenios[-2:]) #Imprimindo os dois ultimos elementos
print('Cl' in halogenios) #Verificando se tem ocorrencia do Cl na tupla. 
#Somar todos os itens da tupla
print(sum(t))
#verificar o menor numero
print(min(t))