import flet as ft

def main(page:ft.Page):
    page.title = "Usando AlertDialogs e Banner"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)
    
    def close_banner(e):
        page.close(banner)
        page.add(ft.Text("Clicado: "+e.control.text))
    
    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            value="OOps, there were some errors while trying to delete the file.",
            color=ft.colors.BLACK,
        ),
        actions=[
            ft.TextButton(text="Retry", style=action_button_style, on_click=close_banner),
            ft.TextButton(text="Ignore",style=action_button_style, on_click=close_banner),
            ft.TextButton(text="Cancel",style=action_button_style, on_click=close_banner)
        ],
    )
    
    def show_non_modal_dialog(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Hi, this is a non-modal dialog!"),
            on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed"))
        )
        page.open(dlg)
        
    def show_modal_dialog(e):
        def handle_close(e):
            page.close(dlg_modal)
            page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
    
        dlg_modal = ft.AlertDialog(
            modal = True,
            title=ft.Text("Please Confirm?"),
            content=ft.Text("DO yo really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_close)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(ft.Text("Modal dialog dismissed"))
        )
    
        page.open(dlg_modal)
        
    page.add(
        ft.Column(
            controls = [
                ft.ElevatedButton("Open non-modal dialog", on_click=show_non_modal_dialog),
                ft.ElevatedButton("Open modal dialog", on_click=show_modal_dialog),
                ft.ElevatedButton("Show banner", on_click=lambda e: page.open(banner))
            ]
        )
    )

ft.app(target=main)