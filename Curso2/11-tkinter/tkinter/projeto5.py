import tkinter
from tkinter import * 
from tkinter import ttk

from PIL import Image, ImageTk

from dados import * 

# Cores
co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#ef5350"

janela = Tk()
janela.title("Pokemon")
janela.geometry("550x510")
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

frame_pokemon = Frame(janela, width=550, height=290, pady=0, padx=0, relief="flat")
frame_pokemon.grid(row=1, column=0)

# Nome
pok_nome = Label(frame_pokemon, text="", relief="flat", anchor="center",
                 font=("Fixedsys 20"), bg=co1, fg=co1)
pok_nome.place(x=12, y=15)

# Tipo
pok_tipo = Label(frame_pokemon, text="", relief="flat", anchor=NW,
                 font=("Ivy 10 bold"), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# Numero
pok_numero = Label(frame_pokemon, text="", relief="flat", anchor="center",
                 font=("Ivy 12"), bg=co1, fg=co1)
pok_numero.place(x=12, y=75)

#Imagem 
img_pokemon = Image.open("img/pikachu.png")
img_pokemon = img_pokemon.resize((238, 238))
img_pokemon = ImageTk.PhotoImage(img_pokemon)

l_icon_1 = Label(frame_pokemon, image=img_pokemon, bg=co1)
l_icon_1.place(x=60, y=50)

# Status
pok_status = Label(janela, text="Status", relief="flat", 
                   font=("Verdana 20"), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(janela, text="HP: 100", relief="flat", anchor="center",
                   font=("Verdana 10"), bg=co1, fg=co4)
pok_hp.place(x=20, y=360)

pok_atack = Label(janela, text="Atack: 300", relief="flat", anchor="center",
                   font=("Verdana 10"), bg=co1, fg=co4)
pok_atack.place(x=20, y=385)

pok_defesa = Label(janela, text="Defesa: 500", relief="flat", anchor="center",
                   font=("Verdana 10"), bg=co1, fg=co4)
pok_defesa.place(x=20, y=410)

pok_velocidade = Label(janela, text="Velocidade: 100", relief="flat", anchor="center",
                   font=("Verdana 10"), bg=co1, fg=co3)
pok_velocidade.place(x=20, y=435)

pok_total = Label(janela, text="Total: 100", relief="flat", anchor="center",
                   font=("Verdana 10"), bg=co1, fg=co3)
pok_total.place(x=20, y=460)

# Habilidades
pok_habilidade = Label(janela, text="Habilidades", relief="flat", anchor="center",
                       font=("Verdana 20"), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

pok_hb_1 = Label(janela, text="Jato d'Água", relief="flat", anchor="center",
                 font=("Verdana 10"), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = Label(janela, text="Hidro Bomba", relief="flat", anchor="center",
                 font=("Verdana 10"), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)

pok_tipo.lift()
pok_numero.lift()

def trocar(i):
    global l_icon_1, img_pokemon
    
    imagem = pokemon[i]['outros'][0]
    img_pokemon = Image.open(imagem)
    img_pokemon = img_pokemon.resize((238, 238))
    img_pokemon = ImageTk.PhotoImage(img_pokemon)
    
    l_icon_1 = Label(janela, image=img_pokemon, width=300,
                     bg=pokemon[i]['outros'][1])
    l_icon_1.place(x=60, y=50)
    
    # tipo pokemon
    pok_nome["text"] = i
    pok_nome["bg"] = pokemon[i]['outros'][1]
    pok_tipo["text"] = pokemon[i]['tipo'][1]
    pok_tipo["bg"] = pokemon[i]['outros'][1]
    pok_numero["text"] = pokemon[i]['tipo'][0]
    pok_numero["bg"] = pokemon[i]['outros'][1]
    
    frame_pokemon["bg"] = pokemon[i]['outros'][1]
    
    # status
    
    pok_hp["text"] = pokemon[i]['status'][0]
    pok_atack["text"] = pokemon[i]['status'][1]
    pok_defesa["text"] = pokemon[i]['status'][2]
    pok_velocidade["text"] = pokemon[i]['status'][3]
    pok_total["text"] = pokemon[i]['status'][4]
    
    # habilidade
    pok_hb_1["text"] = pokemon[i]['habilidades'][0]
    pok_hb_2["text"] = pokemon[i]['habilidades'][1]
    
    pok_tipo.lift()
    pok_numero.lift()
    
# Botões para Pokemon
img_pok_1 = Image.open("img/cabeca-pikachu.png")
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

app_b_1 = Button(janela, command=lambda:trocar('Pikachu'), text="Pikachu",
                 width=150, image=img_pok_1, padx=5, compound=LEFT, relief="raised",
                 overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg=co1, fg=co0)
app_b_1.place(x=375, y=10)

img_pok_2 = Image.open("img/cabeca-bulbasaur.png")
img_pok_2 = img_pok_2.resize((40, 40))
img_pok_2 = ImageTk.PhotoImage(img_pok_2)

app_b_2 = Button(janela, command=lambda:trocar('Bulbasaur'), text="Bulbasaur",
                 width=150, image=img_pok_2, padx=5, compound=LEFT, relief="raised",
                 overrelief=RIDGE, anchor=NW, font=("Verdana 12"), bg=co1, fg=co0)
app_b_2.place(x=375, y=65)

img_pok_3 = Image.open('img/cabeca-charmander.png')
img_pok_3 = img_pok_3.resize((40, 40))
img_pok_3 = ImageTk.PhotoImage(img_pok_3)

app_b_3 = Button(janela,command=lambda:trocar('Charmander'), 
    text="  Charmander", width=150, image=img_pok_3, padx=5, 
    compound=LEFT, relief="raised", overrelief=RIDGE, anchor=NW, 
    font=('Verdana 12'), bg=co1, fg=co0)
app_b_3.place(x=375, y=120)

# ------------
img_pok_4 = Image.open('img/cabeca-gyarados.png')
img_pok_4 = img_pok_4.resize((40, 40))
img_pok_4 = ImageTk.PhotoImage(img_pok_4)

app_b_4 = Button(janela,command=lambda:trocar('Gyarados'), 
    text="  Gyarados", width=150, image=img_pok_4, padx=5, 
    compound=LEFT, relief="raised", overrelief=RIDGE, anchor=NW, 
    font=('Verdana 12'), bg=co1, fg=co0)
app_b_4.place(x=375, y=175)

# ------------
img_pok_5 = Image.open('img/cabeca-gengar.png')
img_pok_5 = img_pok_5.resize((40, 40))
img_pok_5 = ImageTk.PhotoImage(img_pok_5)

app_b_5 = Button(janela,command=lambda:trocar('Gengar'), 
    text="  Gengar", width=150, image=img_pok_5, padx=5, 
    compound=LEFT, relief="raised", overrelief=RIDGE, 
    anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
app_b_5.place(x=375, y=230)

# ------------
img_pok_6 = Image.open('img/cabeca-dragonite.png')
img_pok_6 = img_pok_6.resize((40, 40))
img_pok_6 = ImageTk.PhotoImage(img_pok_6)

app_b_6 = Button(janela,command=lambda:trocar('Dragonite'), 
    text="  Dragonite", width=150, image=img_pok_6, padx=5, 
    compound=LEFT, relief="raised", overrelief=RIDGE, anchor=NW, 
    font=('Verdana 12'), bg=co1, fg=co0)
app_b_6.place(x=375, y=285)


janela.mainloop()