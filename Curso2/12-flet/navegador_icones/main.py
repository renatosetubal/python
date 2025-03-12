import flet as ft 
from Projetos.navegador_icones.icon_container import create_icon_container 

is_dark_mode = False
icons_grid = None

def main(page:ft.Page):
    page.title = "Barra de navegação"
   
    def toggle_dark_mode(event):
        global is_dark_mode
        is_dark_mode = not is_dark_mode
        page.theme_mode=ft.ThemeMode.DARK if is_dark_mode else ft.ThemeMode.LIGHT
        page.update()
    
    def search_icons(event:ft.ControlEvent):
        search_value = event.control.value.upper()
        icons_grid.controls = []
        for icon_name in dir(ft.icons):
            if search_value in icon_name:
                icons_grid.controls.append(create_icon_container(icon_name=icon_name))
        icons_grid.update()
                
        
        
    def show_search_page(event=None):
        page.clean()
        search_bar=ft.TextField(
            prefix_icon=ft.icons.SEARCH,
            hint_text="Digite algo para buscar...",
            on_submit=search_icons 
        )
        
        global icons_grid
        icons_grid = ft.GridView(
            expand=True,
            max_extent=200,
            controls=[],
            child_aspect_ratio=1.0
        )

        layout = ft.Column(
            expand= True, 
            controls=[
                search_bar,
                icons_grid,
                ft.ElevatedButton("Alternar Tema Visual", 
                                  on_click=toggle_dark_mode)
            ]
        )
        page.add(layout)
    page.theme_mode = ft.ThemeMode.LIGHT
    show_search_page()
    
ft.app(target=main, view=ft.AppView.FLET_APP)