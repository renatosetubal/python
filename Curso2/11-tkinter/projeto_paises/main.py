from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import messagebox
from PIL import Image, ImageTk
from random import *
from mod_paises import *

# Cores
co0= "#444466"
co1= "#feffff"
co2= "#6f9fbd"
co3= "#38576b"
co4= "#403d3d"
fundo_cima = "#2aa6a8"
fundo= co1
cor1="#f0ba4f"

#Criacao da Janela
janela = Tk()
janela.title("Qual é o país?")
janela.geometry("350x310")
janela.configure(bg=co1)

#Frames
ttk.Separator(janela,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)
frame_top= Frame(janela, width=350, height=60, bg=fundo_cima,
                 pady=0, padx=0, relief="flat")
frame_top.grid(row=1, column=0)

frame_bottom= Frame(janela, width=350, height=250, bg=co1,
                 pady=12, padx=0, relief="flat")
frame_bottom.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressBar", tickness=5)

global pontos, vida, nome_do_pais, img_bandeira

pontos = 0
vida = 3

app_nome = Label(frame_top, text="Qual o país", relief="flat", 
                 font=("Fixedsys 20"), bg=fundo_cima, fg=co1)
app_nome.place(x=15, y=15)

#Criando a progressBAr
bar = Progressbar(frame_bottom, length=293, style="black.Horizontal.TProgressbar")
bar.place(x=27,y=50)
bar['value'] = pontos

l_score= Label(frame_bottom, text="Pontuação: "+str(pontos), 
               font=("System 17"), bg=fundo, fg=co0)
l_score.place(x=27, y=10)

# Imagens vida
img0 = Image.open("0.png")
img0 = img0.resize((30,30))
img0 = ImageTk.PhotoImage(img0)

img1 = Image.open("1.png")
img1 = img1.resize((30,30))
img1 = ImageTk.PhotoImage(img1)

# Labels dos ícones
licon1 = Label(frame_bottom, image=img1, bg=fundo)
licon1.place(x=229, y=10)

licon2 = Label(frame_bottom, image=img1, bg=fundo)
licon2.place(x=259, y=10)

licon3 = Label(frame_bottom, image=img1, bg=fundo)
licon3.place(x=289, y=10)

# Label para pergunta
lperguntas = Label(frame_bottom, 
                   text="Qual país percente essa bandeira?",
                   pady=0, padx=0, relief="flat", anchor="center",
                   font=("Ivy 10 bold"), bg=co1, fg=co4)
lperguntas.place(x=30,y=70)

#Campo de resposta

resposta=Entry(frame_bottom, width=15, justify="center", 
               font=("",12), highlightthickness=1, relief="solid")
resposta.place(x=178,y=100)

# Funções do jogo

def iniciar_jogo():
    global pontos, vidas, nome_do_pais, licon_bandeira, img_bandeira

    dados = dados_pais()
    nome_do_pais = dados[1]
    imagem = dados[0]
    # Pegando a imagem da bandeira
    img_bandeira = Image.open(imagem)
    img_bandeira = img_bandeira.resize((140,100))
    img_bandeira - ImageTk.PhotoImage(img_bandeira)

    licon_bandeira = Label(frame_bottom, image=img_bandeira, bg=fundo, relief="solid")
    licon_bandeira.place(x=30, y=100)

def reiniciar_jogo():
    global pontos, nome_do_pais, vida, img_0, img_1
    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text="Pontuação: "+str(pontos))
    licon1['image'] = img1
    licon2['image'] = img1
    licon3['image'] = img1
    iniciar_jogo()

def game_over():
    global pontos, nome_do_pais, vida, img_0, img_1
    pontos = 0
    vida = 3
    bar['value'] = pontos
    l_score.configure(text="Pontuação: "+str(pontos))
    licon1['image'] = img1
    licon2['image'] = img1
    licon3['image'] = img1
    iniciar_jogo()

b_resposta=Button(frame_bottom, text="Confirmar", width=10, height=1, bg=co1, fg=co4,
                  font=("Ivy 8 bold"), relief=RAISED, overrelief=RIDGE)
b_resposta.place(x=210,y=150)



janela.mainloop()
