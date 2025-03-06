import csv
file_path="./cursos.csv"
modo="a"
cursos=[]

def add_cursos():
    lin=input("Digite a linguagem: ")
    cat=input("Digite a categoria: ")
    with open(file_path, modo,encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow([lin, cat]) 
        print("Curso adicionado com sucesso!")


add_cursos()