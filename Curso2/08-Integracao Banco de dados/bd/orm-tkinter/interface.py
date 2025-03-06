import tkinter as tk
import orm
from tkinter import messagebox

def adicionar():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.add_filme(nome, ano, nota)
    messagebox.showinfo('Filme Adicionado', 'Filme adicionado com sucesso!')

def atualizar():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.update_filme(id, nome, ano, nota)
    messagebox.showinfo('Filme Atualizado', 'Filme atualizado com sucesso!')

def excluir():
    id = entry_id.get()
    orm.remove_filme(id)
    messagebox.showinfo('Filme Excluído', 'Filme excluído com sucesso!')

#Interface gráfica
root = tk.Tk()
root.title('Gerenciador de Filmes - CRUD')
root.geometry('500x300')

#Rotulos
label_id = tk.Label(root, text='ID:')
label_id.grid(row=0, column=0, padx=10, pady=10)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

label_nome = tk.Label(root, text='Nome:')
label_nome.grid(row=1, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

label_ano = tk.Label(root, text='Ano:')
label_ano.grid(row=2, column=0, padx=10, pady=10)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

label_nota = tk.Label(root, text='Nota:')
label_nota.grid(row=3, column=0, padx=10, pady=10)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

#Botões
button_adicionar = tk.Button(root, text='Adicionar', command=adicionar)
button_adicionar.grid(row=4, column=0, padx=10, pady=10)
button_alterar = tk.Button(root, text='Atualizar', command=atualizar)
button_alterar.grid(row=4, column=1, padx=10, pady=10)
button_excluir = tk.Button(root, text='Excluir', command=excluir)
button_excluir.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
