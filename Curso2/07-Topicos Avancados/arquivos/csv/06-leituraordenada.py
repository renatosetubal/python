file_path="./cursos.csv"
modo="r"
cursos=[]
def ler_ordenado():
    with open(file_path, modo,encoding="utf-8") as file:
        for linha in file:
            linguagem, categoria = linha.strip().split(",")
            cursos.append((linguagem,categoria))
        cursos.sort()

def exibe_cursos():
    ler_ordenado()
    for curso in cursos:
        print(f"A linguagem {curso[0]} serve para {curso[1]}")

exibe_cursos()