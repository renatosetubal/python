file_path="dados/names.txt"
names = []

def exibir_names():
    for name in sorted(names):
        print(name)

def ler():
   with open(file_path, "r",encoding="utf-8") as file:
         for line in file:
              names.append(line.strip())
ler()
exibir_names()