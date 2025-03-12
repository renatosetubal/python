import flet as ft

def main(page:ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()
    
    images = ft.Row(expand=1, wrap=False, scroll="always")
    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(40)
            )
        )
    page.add(images)
    page.update()
ft.app(target=main)