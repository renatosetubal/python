import csv
file_path="./cursos.csv"
modo="r"
cursos=[]
def usocsv():
    with open(file_path, modo,encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for linha in reader:
            cursos.append({
                "linguagem": linha["linguagem"],
                "categoria": linha["categoria"]
            })
    print(cursos)

usocsv()