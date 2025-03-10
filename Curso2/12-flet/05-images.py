import flet as ft 

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    # Adicionando uma imagem
    img = ft.Image(
        src="https://www.w3schools.com/w3images/lights.jpg",
        border_radius=ft.border_radius.all(50),
        width=500, 
        height=500,
        tooltip="Minha imagem de teste"
    )
    page.add(img)
    page.update()
    
ft.app(target=main)