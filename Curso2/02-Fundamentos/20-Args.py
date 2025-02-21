#1 funcao para imprimir nome completo
def full_name(first,middle,last):
    print(f"Nome completo é: {first} {middle} {last}")
full_name("Renato","Miranda", "Setúbal")

#2 Função com parametro default
def endereco(pais="Brazil"):
    print(f'I live in {pais}')

endereco()
endereco("United State of America")