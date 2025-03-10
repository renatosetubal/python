import flet as ft 

def main(page:ft.Page):
   page.title = ("Flet Exemplo")
#    page.bgcolor="#C79030"
   page.bgcolor = ft.colors.AMBER_300
   
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   
   page.padding = ft.padding.all(100)
   
   page.add(
       ft.Text(value="Olá mundo!"),
       ft.Container(ft.Text(value="Hello World"), bgcolor=ft.colors.BLUE_600)
   )
   
   # Desktop
   page.window_height = 300
   page.window_width = 600
   page.window.resizable = False
   
   # Posicionamento de janela
   page.window_top = 100
   page.window_left = 300
   page.window_progress_bar = 1 

   
   page.update()

ft.app(target=main)