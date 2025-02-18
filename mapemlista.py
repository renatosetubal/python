lista_numeros=[1,2,3,4]
def multiplica(x):
    return x * 2

nova_lista= map(multiplica, lista_numeros)
print(list(nova_lista))