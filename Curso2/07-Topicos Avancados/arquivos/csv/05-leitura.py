file_path="./cursos.csv"
modo="r"

def ler_arquivo():
    with open(file_path, modo,encoding="utf-8") as file:
        for linha in file:
            l = linha.strip().split(",")
            print(l[0],l[1])
#Segunda forma de ler o arquivo csv já atribuindo valores
def ler_arquivo2():
    with open(file_path, modo,encoding="utf-8") as file:
        for linha in file:
            linguagem, categoria = linha.strip().split(",")
            print(f"A linguagem {linguagem} serve para {categoria}")


ler_arquivo()
ler_arquivo2()