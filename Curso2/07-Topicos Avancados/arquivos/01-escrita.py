import os
# print(os.getcwd())
file_path="dados/names.txt"
def imp01():
    name = input("Digite o nome do aluno: ")
    file = open(file_path, "a",encoding="utf-8")
    file.write(f"{name}\n")
    file.close()

def imp02():
    name = input("Digite o nome do aluno: ")
    with open(file_path, "a",encoding="utf-8") as file:
        file.write(f"{name}\n")



imp02()
