file_path="./cursos.csv"
modo="r"
cursos=[]
def ler_ordenado():
    with open(file_path, modo,encoding="utf-8") as file:
        for linha in file:
            linguagem, categoria = linha.strip().split(",")
            curso = {}
            curso["linguagem"] = linguagem
            curso["categoria"] = categoria
            cursos.append(curso)
        cursos.sort(key=lambda curso: curso["linguagem"])

def exibe_cursos():
    ler_ordenado()
    for curso in cursos:
        print(f"A linguagem {curso['linguagem']} serve para {curso['categoria']}")

exibe_cursos()