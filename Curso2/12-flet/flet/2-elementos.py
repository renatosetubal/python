import flet as ft

def main(page:ft.Page):
    msg = ft.Text(value="Hello World")
    page.add(msg)

ft.app(target=main)