import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.add(
        ft.CupertinoActivityIndicator(
            radius=50,
            color=ft.colors.RED,
            animating=True
        )
    )

ft.app(target=main)