import flet as ft

def main(page:ft.Page):
    page.title = "NavigationBar"
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_BORDER,
                                        label="Explore",
                                        selected_icon=ft.icons.BOOKMARK
                                        ),
        ]
    )
    page.add(ft.Text("Body"))

ft.app(target=main)