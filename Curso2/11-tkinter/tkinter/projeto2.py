from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import Image, ImageTk
from random import *
from paises import * 

# Cores
co0 = "#444466" # Preta
co1 = "#feffff" # branca
co2 = "#6f9fbd" # azul
co3 = "#38576b"
co4 = "#403d3d"
fundo_cima = "#2aa6a8"

fundo = co1
cor1 = "#f0ba4f"

janela = Tk()
janela.title("Qual país")
janela.geometry("350x310")
janela.configure(bg=co1)

# Frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)

frame_cima = Frame(janela, width=350, height=60, bg=fundo_cima,
                   pady=0, padx=0, relief="flat")
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=350, height=300, bg=fundo,
                   pady=12, padx=0, relief="flat")
frame_baixo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressBar", thickness=5)

global pontos, vida, nome_do_pais, img_bandeira

pontos = 0
vida = 3

app_nome  = Label(frame_cima, text="QUAL O PAÍS?", relief="flat",
                  anchor="center", font=("Fixedsys 20"), bg=fundo_cima, fg=co1)
app_nome.place(x=15, y=15)

bar = Progressbar(frame_baixo, length=293, style="black.Horizontal.TProgressbar")
bar.place(x=27, y=50)
bar['value'] = pontos

l_score = Label(frame_baixo, text="Pontuação: "+str(pontos), 
                font=("System 17"), bg=fundo, fg=co0)
l_score.place(x=27, y=10)

# Imagens vida
img_0 = Image.open("0.png")
img_0 = img_0.resize((30, 30))
img_0 = ImageTk.PhotoImage(img_0)

img_1 = Image.open("1.png")
img_1 = img_1.resize((30, 30))
img_1 = ImageTk.PhotoImage(img_1)

l_icon_1 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_1.place(x=229, y=10)

l_icon_2 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_2.place(x=259, y=10)

l_icon_3 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_3.place(x=289, y=10)

# Label para Pergunta
l_perguntas = Label(frame_baixo,
                    text="Qual país pertence essa bandeira?",
                    pady=0, padx=0, relief="flat", anchor="center",
                    font=("Ivy 10 bold"), bg=co1, fg=co4)
l_perguntas.place(x=30, y=70)

# Campo para Resposta
e_resposta = Entry(frame_baixo, width=15, justify="center", 
                   font=("", 12), highlightthickness=1, relief="solid")
e_resposta.place(x=178, y=100)

def iniciar_jogo():
    global pontos, vida, nome_do_pais, l_icon_bandeira, img_bandeira
    
    dados = dados_pais()
    nome_do_pais = dados[1]
    imagem = dados[0]
    
    # Imagem bandeira
    img_bandeira = Image.open(imagem)
    img_bandeira = img_bandeira.resize((140, 100))
    img_bandeira = ImageTk.PhotoImage(img_bandeira)
    
    l_icon_bandeira = Label(frame_baixo, image=img_bandeira, bg=fundo, relief="solid")
    l_icon_bandeira.place(x=30, y=100)
    
def reiniciar_jogo():
    global pontos, nome_do_pais, vida, img_0, img_1
    
    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text="Pontuação: "+str(pontos))
    l_icon_1['image'] = img_1
    l_icon_2['image'] = img_1
    l_icon_3['image'] = img_1
    
    iniciar_jogo()

def game_over():
    global pontos, nome_do_pais, vida, img_0, img_1

    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text="Pontuação: "+str(pontos))
    l_icon_1['image'] = img_1
    l_icon_2['image'] = img_1
    l_icon_3['image'] = img_1
    
    iniciar_jogo()

def verificar():
    global pontos, vida
    
    resposta = e_resposta.get()
    if resposta == nome_do_pais:
        pontos += 10
        l_score.configure(text="Pontuação: " + str(pontos))
        bar['value'] = pontos
        e_resposta.delete(0, END)   
    else:
        messagebox.showerror("Erro", "Resposta está incorreta!")
        vida -= 1
        if vida == 2:
            l_icon_1['image'] = img_0
        if vida == 1:
            l_icon_2['image'] = img_0
        if vida == 0:
            l_icon_3['image'] = img_0
        if vida == -1:
            messagebox("Game Over", "Fim do jogo!")
            game_over()
        e_resposta.delete(0, END)
    
    if bar['value'] == 100:
        messagebox.showinfo("Parabéns", "Parabéns você venceu o jogo!")
        reiniciar_jogo()
    else:
        iniciar_jogo()
            
            
b_resposta = Button(frame_baixo, text="Confirmar", width=10, height=1, bg=co1, fg=co4,
                    font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE, command=verificar)
b_resposta.place(x=210, y=150)
    
iniciar_jogo()

janela.mainloop()