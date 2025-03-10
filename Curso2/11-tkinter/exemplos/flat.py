import tkinter as tk

janela = tk.Tk()
label1 = tk.Label(janela, text="Label com relief flat", relief="flat")
label2 = tk.Label(janela, text="Label com relief raised", relief="raised")
label3 = tk.Label(janela, text="Label com relief sunken", relief="sunken")

label1.pack(pady=10)
label2.pack(pady=10)
label3.pack(pady=10)

janela.mainloop()