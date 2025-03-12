import flet as ft

def main(page: ft.Page):
    page.title = "Exemplo de Tabela com Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Criando os dados da tabela
    data = [
        {"id": 1, "nome": "João Silva", "email": "joao.silva@exemplo.com", "cargo": "Desenvolvedor"},
        {"id": 2, "nome": "Maria Santos", "email": "maria.santos@exemplo.com", "cargo": "Designer"},
        {"id": 3, "nome": "Pedro Oliveira", "email": "pedro.oliveira@exemplo.com", "cargo": "Gerente de Projeto"},
        {"id": 4, "nome": "Ana Costa", "email": "ana.costa@exemplo.com", "cargo": "Analista de Dados"},
        {"id": 5, "nome": "Carlos Souza", "email": "carlos.souza@exemplo.com", "cargo": "Desenvolvedor"},
    ]
    
    # Criar o SnackBar uma vez
    snack = ft.SnackBar(content=ft.Text(""))
    page.add(snack)  # Adicionar o SnackBar à página
    
    # Função para lidar com o clique em uma linha
    def row_clicked(e):
        row_data = e.control.data
        # Atualizar e mostrar o SnackBar
        snack.content = ft.Text(f"Clicou em: {row_data['nome']} ({row_data['cargo']})")
        snack.open = True
        page.update()
    
    # Criando a tabela
    table = ft.DataTable(
        border=ft.border.all(1, ft.colors.GREY_400),
        vertical_lines=ft.border.BorderSide(1, ft.colors.GREY_400),
        horizontal_lines=ft.border.BorderSide(1, ft.colors.GREY_400),
        columns=[
            ft.DataColumn(
                ft.Text("ID", weight=ft.FontWeight.BOLD),
                numeric=True
            ),
            ft.DataColumn(
                ft.Text("Nome", weight=ft.FontWeight.BOLD),
            ),
            ft.DataColumn(
                ft.Text("Email", weight=ft.FontWeight.BOLD),
            ),
            ft.DataColumn(
                ft.Text("Cargo", weight=ft.FontWeight.BOLD),
            ),
        ],
        rows=[]
    )
    
    # Adicionando linhas à tabela com base nos dados
    for item in data:
        # Criando uma linha
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(item["id"]))),
                ft.DataCell(ft.Text(item["nome"])),
                ft.DataCell(ft.Text(item["email"])),
                ft.DataCell(ft.Text(item["cargo"])),
            ],
            on_select_changed=row_clicked,
            data=item  # Salvando os dados completos da linha
        )
        table.rows.append(row)
    
    # Adicionando título e a tabela à página usando uma coluna centralizada
    page.add(
        ft.Column(
            [
                ft.Text("Lista de Funcionários", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=table,
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente
            expand=True  # Expande para preencher toda a página
        )
    )

ft.app(target=main)