import tkinter as tk
from tkinter import messagebox

# Função para mostrar mensagem quando um item do menu for clicado
def mostrar_mensagem(mensagem):
    messagebox.showinfo("Informação", mensagem)

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Menus no Tkinter")
janela.geometry("400x300")

# Criar a barra de menu
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)

# Criar o menu Arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Adicionar itens ao menu Arquivo
menu_arquivo.add_command(label="Novo", command=lambda: mostrar_mensagem("Novo arquivo criado!"))
menu_arquivo.add_command(label="Abrir", command=lambda: mostrar_mensagem("Abrir arquivo"))
menu_arquivo.add_separator()  # Adiciona uma linha separadora
menu_arquivo.add_command(label="Salvar", command=lambda: mostrar_mensagem("Arquivo salvo!"))
menu_arquivo.add_command(label="Salvar como...", command=lambda: mostrar_mensagem("Salvar como..."))
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=janela.quit)

# Criar o menu Editar
menu_editar = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Adicionar itens ao menu Editar
menu_editar.add_command(label="Cortar", command=lambda: mostrar_mensagem("Cortar"))
menu_editar.add_command(label="Copiar", command=lambda: mostrar_mensagem("Copiar"))
menu_editar.add_command(label="Colar", command=lambda: mostrar_mensagem("Colar"))

# Criar o menu Ajuda
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=lambda: mostrar_mensagem("Exemplo de menus no Tkinter"))

# Criar um submenu dentro do menu Editar
submenu = tk.Menu(menu_editar, tearoff=0)
menu_editar.add_cascade(label="Opções avançadas", menu=submenu)
submenu.add_command(label="Opção 1", command=lambda: mostrar_mensagem("Opção avançada 1"))
submenu.add_command(label="Opção 2", command=lambda: mostrar_mensagem("Opção avançada 2"))

# Iniciar o loop principal da aplicação
janela.mainloop()
