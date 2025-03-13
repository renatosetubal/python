import flet as ft

footer_color = ft.colors.BLUE_GREY_800

footer = ft.Container(
            content=ft.Row(
                [
                    ft.Text("© 2025 Gerenciamento de Usuários. Todos os direitos reservados.", color=ft.colors.WHITE),
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
    
