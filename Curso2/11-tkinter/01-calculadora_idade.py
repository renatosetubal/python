from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

#cores
color1="#3b3b3b" #preta / escura
color2="#333333" # preta /clara
color3="#FFFFFF" # branco
color4="#fcc058"

win = Tk()
win.title("Calculadora de Idade")
win.geometry("310x410")
win.configure(bg=color1)

style = ttk.Style(win)
style.theme_use("clam")

# Definindo os frames
top_frame = Frame(win, width=310, height=140, 
                  pady=0, padx=0, relief="flat",bg=color2)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(win, width=310, height=410, 
                  pady=0, padx=0, relief="flat",bg=color1)
bottom_frame.grid(row=1, column=0, sticky=NW)

# Fim definição de Frames

# Labs Top Frame
app_calculator = Label(top_frame, text="Calculadora de", width=25, height=1, padx=3,
                       relief="flat", anchor="center", font=("Ivy 15 bold"),
                       bg=color2, fg=color3)
app_calculator.place(x=0, y=30)

app_off_rage = Label(top_frame, text="Idade", width=11, height=1, padx=0,
                       relief="flat", anchor="center", font=("Arial 35 bold"),
                       bg=color2, fg=color4)
app_off_rage.place(x=0, y=70)

# Labels Bottom Frame
l_initial_date = Label(bottom_frame, text="Data Atual", height=1, padx=0, pady=0, 
                       relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_initial_date.place(x=50, y=30)

cal_initial_date = DateEntry(bottom_frame, width=10, background="darkblue", foreground="white", 
                             borderwidth=2, date_pattern="mm/dd/y", year=2024)
cal_initial_date.place(x=170, y=30)

l_birth_date = Label(bottom_frame, text="Data Aniversário", height=1, padx=0,  
                       relief="flat", anchor=NW, font=("Ivy 9"), bg=color1, fg=color3)
l_birth_date.place(x=50, y=70)

cal_birth_date = DateEntry(bottom_frame, width=10, background="darkblue", foreground="white", 
                             borderwidth=2, date_pattern="mm/dd/y", year=1981)
cal_birth_date.place(x=170, y=70)

app_years = Label(bottom_frame, text="27", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 25 bold"), bg=color1, fg=color3)
app_years.place(x=60, y=135)

app_label_years = Label(bottom_frame, text="Years", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_label_years.place(x=50, y=175)

app_months = Label(bottom_frame, text="27", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 12 bold"), bg=color1, fg=color3)
app_months.place(x=140, y=135)

app_label_months = Label(bottom_frame, text="Months", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_label_months.place(x=130, y=175)

app_days = Label(bottom_frame, text="27", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 12 bold"), bg=color1, fg=color3)
app_days.place(x=220, y=135)

app_label_days = Label(bottom_frame, text="Days", height=1, padx=0,  
                       relief="flat", anchor="center", font=("Ivy 11 bold"), bg=color1, fg=color3)
app_label_days.place(x=210, y=175)


# Função para calculo
def calcular_idade():
    inicial= cal_initial_date.get()
    print(inicial)
    aniversario=cal_birth_date.get()
    dia1, mes1, ano1 = [int(f) for f in inicial.split("/")]
    data_inicial=date(ano1, mes1, dia1)
    dia2, mes2, ano2 = [int(f) for f in aniversario.split("/")]
    data_aniversario=date(ano2, mes2, dia2)
    
    years = relativedelta(data_inicial, data_aniversario).years
    months = relativedelta(data_inicial, data_aniversario).months
    days = relativedelta(data_inicial, data_aniversario).days
    print(f'{years} - {months} - {days}')
   
    app_years.config(text=years)
    app_months.config(text=months)
    app_days.config(text=days)
    
    
#Criando botao
bt_calcular= Button(bottom_frame, text="Calcular", width=20, height=1,
                    bg=color1, fg=color3, font=("Ivy 10 bold"), relief=RAISED, 
                    overrelief=RIDGE, command=calcular_idade)
bt_calcular.place(x=60, y=225)

# Fim Labels Bottom Frame
win.mainloop()