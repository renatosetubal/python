import flet as ft

def create_icon_container(icon_name: str, on_favorite: callable) -> ft.Container:
    favorite_button = ft.IconButton(
        icon=ft.icons.STAR_OUTLINE,
        on_click=lambda e: on_favorite(icon_name)
    )
    return ft.Container(
        padding=ft.padding.all(20),
        bgcolor=ft.colors.WHITE10,
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(name=icon_name, size=50),
                ft.Text(value=icon_name),
                favorite_button
            ]
        )
    )