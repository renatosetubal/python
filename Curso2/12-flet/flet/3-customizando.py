import flet as ft

def main(page:ft.Page):
    page.title = "Flet Exemplo"
    # page.bgcolor = "red"
    # page.bgcolor = "#C79030"
    page.bgcolor = ft.colors.GREEN_ACCENT_700
    
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    page.padding = ft.padding.all(100)
    
    page.add(
        ft.Text(value="Hello WOrld"),
        ft.Container(ft.Text(value="Hello World 2"), bgcolor="black")  
    )
    
    # Desktop
    page.window_height = 300
    page.window_width = 600
    page.window.resizable = False
    
    # Posicionamento da janela
    page.window_top = 300
    page.window_left = 300
    
    page.window_progress_bar = 1
    
    page.update()

ft.app(target=main)