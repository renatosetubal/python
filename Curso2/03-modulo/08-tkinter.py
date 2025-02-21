import tkinter as tk 

#1 - Criar Janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciamento de frases")

#2 - Adicionar um frame
frame = tk.Frame(window)
frame.pack(padx=10,pady=10,fill='x', expand=True)

#3 - Adicionar o label
label = tk.Label(frame,text="Olá Tkinter")
label.pack(fill="x", expand=True)

# 4 - Adicionando o inputtext
frase_lab = tk.Label(frame,text="Frase")
frase_lab.pack(fill='x',expand=True)

frase_imp=tk.Entry(frame)
frase_imp.pack(fill='x',expand=True)

#5 Funcao para alterar o label
def click():
    label.config(text=frase_imp.get())

#6 - Adicionando botao
button = tk.Button(frame,text="Enviar", command=click)
button.pack()


window.mainloop()