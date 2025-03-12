import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def handle_dismissal(e):
        page.add(ft.Text("Drawer dismissed"))
    
    def handle_change(e):
        page.add(ft.Text(f"Selected Index changed: {e.selected_index}"))
        
    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls = [
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon = ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR)
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="Item 2",
                icon_content = ft.Icon(ft.icons.MAIL_OUTLINED),
                selected_icon =ft.icons.MAIL
            ),
            ft.NavigationDrawerDestination(
                label="Item 3",
                icon_content = ft.Icon(ft.icons.PHONE_OUTLINED),
                selected_icon =ft.icons.PHONE
            ),
        ]
    )
    
    page.add(ft.ElevatedButton("Show drawer", on_click=lambda e: page.open(drawer)))

ft.app(target=main)