import os

def add():
    name=input("Digite o nome do contato: ")
    email=input("Digite o email do contato: ")
    phone=input("Digite o telefone do contato: ")
    contato = f"Nome: {name}\nEmail: {email}\nTelefone: {phone}\n"
    with open("dados/contatos.txt", "a",encoding="utf-8") as file:
        file.write(contato)

def lista():
    if not os.path.exists("dados/contatos.txt"):
        print("Ainda não há contatos cadastrados.")
        return
    else:
         with open("dados/contatos.txt", "r",encoding="utf-8") as file:
            contatos=file.read()
            print(contatos)

def remove():
    name = input("Digite o nome do contato que deseja remover: ")
    with open("dados/contatos.txt", "r",encoding="utf-8") as file:
        contatos = file.readlines()
    with open("dados/contatos.txt", "w",encoding="utf-8") as file:
        for contato in contatos:
            if name not in contato:
                file.write(contato)
    print(f"Contato {name} removido com sucesso!")