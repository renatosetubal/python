import flet as ft

def main(page:ft.Page):
    icons_row = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK, size=30),
            ft.Icon(name=ft.icons.AUDIO_FILE, color=ft.colors.GREEN_400, size=30),
            ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.BLUE, size=30),
            ft.Icon(name="settings", color="#c1c1c1", size=30),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    page.add(
        ft.Column(
            controls=[
                icons_row
            ]
        )
    )

ft.app(target=main)