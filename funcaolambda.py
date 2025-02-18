#Exemplo de função lambda.

def retona_lambda(x):
    resultado = lambda x: x + 10
    return resultado(x) * 4

resultado=lambda x: x + 10
resultado2=lambda x, y: x * y
print(resultado(5))
print()
print(resultado2(5, 6))
print(retona_lambda(5))