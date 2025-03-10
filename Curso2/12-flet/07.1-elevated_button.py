import flet as ft 

def main(page:ft.Page):
    page.title = "Exemplo simples"
    page.add(
        ft.ElevatedButton(text="Botão Simples"),
        ft.ElevatedButton("Botão Desabilitado", disabled=True),
        ft.ElevatedButton(text="Botão com ícone", icon="access_time"),
        ft.ElevatedButton("Botão Ícone colorido", icon="park_rounded", icon_color="green600")
    )
    
    def button_clicked(e):
        b.data +=1
        t.value = f"Botão clicado {b.data} vezes"
        page.update()
    b = ft.ElevatedButton("Botão Clicado", on_click=button_clicked, data=0)
    t = ft.Text()
    page.add(b,t)
    
    page.update()
ft.app(target=main)