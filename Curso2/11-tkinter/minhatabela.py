import tkinter as tk
from tkinter import ttk
from tkinter import *
from functions import carregar_dados


#cores
color1="#3b3b3b" #preta / escura
color2="#333333" # preta /clara
color3="#FFFFFF" # branco
color4="#fcc058"

win = Tk()
win.title("Calculadora de Idade")
win.geometry("600x410")
win.configure(bg=color1)

style = ttk.Style(win)
style.theme_use("clam")

# Definindo os frames
top_frame = Frame(win, width=600, height=140, 
                  pady=0, padx=0, relief="flat",bg=color2)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(win, width=310, height=410, 
                  pady=0, padx=0, relief="flat",bg=color1)
bottom_frame.grid(row=1, column=0, sticky=NW)

## FIM FRAMES



# Cria o Treeview

style.configure("Treeview", 
               background="#f0f0f0",
               fieldbackground="white",
               foreground="black",
               font=("Arial", 10),
               rowheight=60
               )
tree = ttk.Treeview(
    bottom_frame,
    columns=("ID", "Nome", "Idade", "Cidade"),
    show="headings",
    style="Treeview"  # Aplica o estilo configurado
)

# Define as colunas e seus cabeçalhos
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Cidade", text="Cidade")

# Configura o tamanho das colunas
tree.column("ID", width=20, anchor="center")
tree.column("Nome", width=250)
tree.column("Idade", width=80, anchor="center")
tree.column("Cidade", width=250)
tree.pack(side="top", fill="both", expand=True)

# Função para obter o item selecionado
def item_selecionado(event):
    selected = tree.selection()
    if selected:
        item = tree.item(selected)
        print("Item selecionado:", item["values"])
# Associa o evento de clique no Treeview
tree.bind("<<TreeviewSelect>>", item_selecionado)

btn_carregar = ttk.Button(top_frame, text="Carregar Dados", command=carregar_dados(tree))
btn_carregar.pack(pady=10)

win.mainloop()