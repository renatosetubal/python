# Importar biblioteca
import random

#Iniciando lista onde iremos guardar os números gerados 
lista = []

#Tamanho limite que queremos gerar
tamanho_lista = 6

# Iniciando contador para controle
i = 0

#Loop para gerar 10 números
while i < 6:
    lista.append(random.randint(1,60))
    i = i + 1

# Printando lista
print(lista)