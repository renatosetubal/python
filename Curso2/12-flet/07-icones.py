import flet as ft 

def main(page:ft.Page):
    icons_row = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.BLUE),
            ft.Icon(name=ft.icons.AUDIO_FILE, color=ft.colors.RED),
            ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.GREEN),
            ft.Icon(name=ft.icons.ACCESS_ALARM, color=ft.colors.ORANGE_500)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )
    page.add(
        ft.Column(
            controls=[
                icons_row
            ]
        )
    )
        
ft.app(target=main)