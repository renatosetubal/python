import flet as ft 

def main(page:ft.Page):
    page.title = "Barra de navegação"
    
    page.add(ft.Texx("Corpo do sistema"))
ft.app(target=main)