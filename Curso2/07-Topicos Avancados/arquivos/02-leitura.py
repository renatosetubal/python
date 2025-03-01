file_path="dados/names.txt"
def ler01():
   with open(file_path, "r",encoding="utf-8") as file:
        print(file.read())
def ler02():
   with open(file_path, "r",encoding="utf-8") as file:
         for line in file:
              print(f"Olá {line.strip()}. Seja bem vindo")


ler02()