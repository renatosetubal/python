import flet as ft

def main(page: ft.Page):
    page.title = "Aplicativo de Três Camadas"
    page.padding = 0  # Remove o padding padrão para usar toda a tela
    
    # Configurando cores para cada seção
    menu_color = ft.colors.BLUE_700
    content_color = ft.colors.WHITE
    footer_color = ft.colors.BLUE_GREY_800
    
    # Criando itens de menu
    def menu_item_clicked(e):
        # Atualiza o conteúdo quando um item de menu é clicado
        content_text.value = f"Conteúdo da seção: {e.control.text}"
        page.update()
    
    menu_items = [
        ft.TextButton(text="Pesquisar", on_click=menu_item_clicked),
        ft.TextButton(text="Cadastrar", on_click=menu_item_clicked),
        ft.TextButton(text="Desativar", on_click=menu_item_clicked),
        ft.TextButton(text="Listar", on_click=menu_item_clicked),
        ft.TextButton(text="Contato", on_click=menu_item_clicked),
    ]
    
    # Para cada botão no menu, defina a cor do texto como branca
    for item in menu_items:
        item.style = ft.ButtonStyle(color=ft.colors.WHITE)
    
    # 1. Menu (Camada Superior)
    menu = ft.Container(
        content=ft.Row(
            [
                ft.Text("Meu Aplicativo", color=ft.colors.WHITE, size=22, weight=ft.FontWeight.BOLD),
                # Espaçador para empurrar o texto para a esquerda e os botões para a direita
                ft.Container(expand=True),
                # Itens de menu em uma linha
                *menu_items,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor=menu_color,
        height=60,
    )
    
    # 2. Conteúdo (Camada do Meio)
    escolha_pesquisa=ft.RadioGroup(
                content=ft.Row([
                ft.Radio(value="0", label="Matrícula"),
                ft.Radio(value="1", label="Por Nome")
            ], spacing=20)
        )
    text_input = ft.TextField(
        # label="Busca", 
        hint_text="Digite a busca", 
        width=300,
        border_color=ft.colors.BLUE_500
    )
    botao_pesquisa=ft.ElevatedButton(
                width=200,
                height=50,
                
                content=ft.Row(
                    [
                        # ft.Icon(name=ft.icons.SEARCH_ROUNDED, color=ft.colors.BLUE),
                        ft.Text("Pesquisar...")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                on_click=lambda e: print(f"Valor digitado:{escolha_pesquisa.value}")
    )
    
    linha_pesquisa = ft.Row([
        escolha_pesquisa,
        text_input,   
        botao_pesquisa
        ], spacing=30
    )  # Espaçamento entre o RadioGroup e o TextField
    
 
    
    content_text = ft.Text(
        "Conteúdo principal do aplicativo. Clique em um item do menu para mudar este conteúdo.",
        size=16,
    )
    
    content = ft.Container(
        content=ft.Column(
            [
                linha_pesquisa,
                ft.ElevatedButton("Clique-me!", on_click=lambda e: print("Botão clicado!")),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20,
        ),
        padding=30,
        # bgcolor=content_color,
        expand=True,  # Isso faz o conteúdo expandir e ocupar todo o espaço disponível
    )
    
    # 3. Rodapé (Camada Inferior)
    footer = ft.Container(
        content=ft.Row(
            [
                ft.Text("© 2025 Meu Aplicativo. Todos os direitos reservados.", color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.Row(
                    [
                        ft.TextButton("Política de Privacidade", style=ft.ButtonStyle(color=ft.colors.WHITE)),
                        ft.TextButton("Termos de Uso", style=ft.ButtonStyle(color=ft.colors.WHITE)),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor=footer_color,
        height=50,
    )
    
    # Organizando as três camadas em uma coluna
    page.add(
        ft.Column(
            [
                menu,           # Camada Superior (Menu)
                content,        # Camada do Meio (Conteúdo)
                footer,         # Camada Inferior (Rodapé)
            ],
            spacing=0,  # Remove o espaçamento entre as camadas
            expand=True,  # Expande para ocupar toda a página
        )
    )

ft.app(target=main)