def carregar_dados(tree):
    # Dados de exemplo (ID, Nome, Idade, Cidade)
    dados = [
        (1, "João", 28, "São Paulo"),
        (2, "Maria", 34, "Rio de Janeiro"),
        (3, "Carlos", 25, "Belo Horizonte"),
        (4, "Ana", 31, "Curitiba"),
    ]

    # Limpa o Treeview antes de inserir novos dados
    for item in tree.get_children():
        tree.delete(item)

    # Insere os dados
    for item in dados:
        tree.insert("", "end", values=item)

