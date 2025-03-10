import tkinter as tk
from tkinter import ttk

# Função para preencher o Treeview com dados de exemplo
def carregar_dados():
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

# Função para obter o item selecionado
def item_selecionado(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected)
        print("Item selecionado:", item["values"])

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo Treeview")
root.geometry("600x400")

# Cria o Treeview
tree = ttk.Treeview(root, columns=("ID", "Nome", "Idade", "Cidade"), show="headings")

# Define as colunas e seus cabeçalhos
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Cidade", text="Cidade")

# Configura o tamanho das colunas
tree.column("ID", width=50, anchor="center")
tree.column("Nome", width=150)
tree.column("Idade", width=50, anchor="center")
tree.column("Cidade", width=150)

# Adiciona uma barra de rolagem vertical
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Adiciona uma barra de rolagem horizontal
scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=scrollbar_x.set)

# Posiciona os widgets na janela
tree.pack(side="bottom", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")

# Botão para carregar dados
btn_carregar = ttk.Button(root, text="Carregar Dados", command=carregar_dados)
btn_carregar.pack(pady=10)

# Associa o evento de clique no Treeview
tree.bind("<<TreeviewSelect>>", item_selecionado)

# Inicia a aplicação
root.mainloop()