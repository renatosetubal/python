import flet as ft 

def main(page:ft.Page):
    page.title = "Barra de navegação"
    page.navigation_bar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Pesquisar"),
            ft.NavigationBarDestination(icon=ft.icons.UMBRELLA, label="Usuários"),
            ft.NavigationBarDestination(icon=ft.icons.GROUP, 
                                        label="Grupos",
                                        selected_icon=ft.icons.GROUP),
        ]    
    )
    page.add(ft.Text("Corpo do sistema"))
ft.app(target=main)