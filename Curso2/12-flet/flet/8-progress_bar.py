import flet as ft
from time import sleep

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    pb = ft.ProgressBar(width=400)
    
    page.add(
        ft.Text("Progresso Linear", style="headlineSmall"),
        ft.Column([ft.Text("Aguarde..."), pb]),
        ft.Text("Progresso Indeterminado", style="headlineSmall"),
        ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee") 
    )
    
    for i in range(0, 101):
        pb.value = i*0.01
        sleep(0.1)
        page.update()

ft.app(target=main)