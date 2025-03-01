import agenda as ag

def main():
    while True:
        print("\n1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            ag.add()
        elif escolha == "2":
            ag.lista()
        elif escolha == "3":
            ag.remove()
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()