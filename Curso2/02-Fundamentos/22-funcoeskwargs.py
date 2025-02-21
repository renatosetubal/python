"""
    *args - Quando você quer receber parâmetros mas não sabe quantos.
    São argumentos passados como tupla.
    **kwargs - Além dos valores pode passar também as respectivas chaves para cada argumento 
    Passados como dicionario
"""

def sum(*num):
    total=0
    for n in num:
        total += n
    print(f"Soma é: {total}")

sum(7,9,9)

def apresentacao(**data):
    for k, value in data.items():
        print(f"{k} - {value}")

print("Lista de Cursos:")
apresentacao(Name="Filosofia",Categoria="Humanas", Level="Avançado" )