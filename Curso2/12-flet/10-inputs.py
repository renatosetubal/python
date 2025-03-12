import flet as ft 

def main(page:ft.Page):
    page.title = "Utilizando diveros Inputs"
    
    text_input = ft.TextField(
        label = "Nome", 
        hint_text="Digite o seu nome", 
        width=300,
        border_color=ft.colors.BLUE_500
    )
    password_input = ft.TextField(
        label="Senha",
        hint_text="Digite a sua senha",
        password=True,
        width=300,
        border_color=ft.colors.RED_300
    )
    
    rg = ft.RadioGroup(
        content = ft.Column([
            ft.Radio(value="red", label="Red"),
            ft.Radio(value="gren", label="Green"),
            ft.Radio(value="blue", label="Blue")
        ])
    )
    
    checkbox = ft.Checkbox(
        label="Aceito os termos e condições?",
        value=False,
        on_change=lambda e: print(f'Checkbox estado: {e.control.value}')
    )
    
    t = ft.Text()
    
    def button_clicked(e):
        t.value = f'Sua cor favorita é: {rg.value}'
        page.update()
    
    color_button = ft.ElevatedButton(
        text="Enviar",
        on_click=button_clicked, 
    )
    
    dropdown = ft.Dropdown(
        label = "Escolha uma opção",
        width=300,
        options=[
            ft.dropdown.Option("Opção 1"),
            ft.dropdown.Option("Opção 2"),
            ft.dropdown.Option("Opção 3"),
        ],
            on_change=lambda e: print(f'Opção selecionada: {e.control.value}')
    )
    
    
    page.add(
        ft.Column(
            controls = [
                text_input,
                password_input,
                checkbox,
                rg,
                t,
                color_button,
                dropdown
            ]
        )
        
    )
    
    page.update()
    
ft.app(target=main)