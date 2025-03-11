import flet as ft 

def main(page:ft.Page):
    page.title = "Exemplo simples"
    page.add(
        ft.ElevatedButton(text="Botão Simples"),
        ft.ElevatedButton("Botão Desabilitado", disabled=True),
        ft.ElevatedButton(text="Botão com ícone", icon="access_time"),
        ft.ElevatedButton("Botão Ícone colorido", icon="park_rounded", icon_color="green600")
    )
    
    def button_clicked(e):
        b.data +=1
        t.value = f"Botão clicado {b.data} vezes"
        page.update()
    b = ft.ElevatedButton("Botão Clicado", on_click=button_clicked, data=0)
    t = ft.Text()
    page.add(b,t)

    page.add(
        ft.ElevatedButton(
            width=150,
            content=ft.Row(
                [
                   ft.Icon(name=ft.icons.FAVORITE, color="yellow"), 
                   ft.Icon(name=ft.icons.AUDIOTRACK, color="blue"), 
                   ft.Icon(name=ft.icons.BEACH_ACCESS, color="green"), 
                ],
            ),
        ),
        ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Botão Composto", size=20),
                        ft.Text(value="Texto Secundário", size=20),
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                ),
                padding=ft.padding.all(10)
            )
        )
    )
    
    page.update()
ft.app(target=main)