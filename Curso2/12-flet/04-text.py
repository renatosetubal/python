import flet as ft 

def main(page:ft.Page):
    t1 = ft.Text(
        value = "Utilizando Elemento de Texto", 
        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
        bgcolor=ft.colors.WHITE12, 
        style= ft.TextStyle(
            color = ft.colors.BLACK38,
            font_family="Arial",
            italic=True,
            weight=ft.FontWeight.W_300
        ), max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        text_align=ft.TextAlign.CENTER
    )
    
    estilo1 = ft.TextStyle(
        color=ft.colors.YELLOW_600
    )
    estilo2 = ft.TextStyle(
        color=ft.colors.BLUE_600,
        decoration=ft.TextDecoration.LINE_THROUGH
    )
    
    t2 = ft.Text(
        spans = [
            ft.TextSpan(text="Texto de exemp em span", url="http://globo.com", style=estilo1),
            ft.TextSpan(text="Continuação do texto", style=estilo2)
            
        ]
    )
    
    page.add(t1, t2)
    page.update
    
ft.app(target=main)