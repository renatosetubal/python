import flet as ft

def main(page:ft.Page):
    # Lista de perguntas e respostas
    faq_items = [
        {
            "question": "O que é o Flet?",
            "answer": "FLet é uma biblioteca Python para criação de interfaces gráficas de forma simples e rápida"
        },
        {
            "question": "Como instalar o Flet?",
            "answer": "VOcê pode instalar o Flet usando o pip: 'pip install flet'. "
        },
        {
            "question": "Onde posso encontrar a documentação?",
            "answer": "A documentação está no link: 'https://flet.dev/docs'"
        }
    ]
    
    def handle_change(e: ft.ControlEvent):
        print(f"Panel {e.data} toggled")
        
    def handle_delete(e: ft.ControlEvent):
        panel.controls.remove(e.control.data)
        page.update()
    
    panel = ft.ExpansionPanelList(
        expand_icon_color=ft.colors.AMBER,
        elevation=8,
        divider_color=ft.colors.AMBER,
        on_change=handle_change
    )
    
    for item in faq_items:
        exp = ft.ExpansionPanel(
            header=ft.ListTile(title=ft.Text(item["question"]))
        )
        
        exp.content = ft.Column(
            [
                ft.ListTile(
                    title=ft.Text(item["answer"])
                ),
                ft.Row(
                    [
                        ft.TextButton("Marcar como útil",
                                      on_click=lambda e, item=item: page.add(
                                          ft.Text(f"Você marcou a resposta: {item['answer']} como útil",
                                                  color=ft.colors.GREEN_600)
                                      )),
                        ft.IconButton(ft.icons.DELETE,
                                      on_click=handle_delete, data=exp)
                    ],
                    alignment=ft.MainAxisAlignment.END
                )
            ]
        )
        panel.controls.append(exp)
    page.add(panel)

ft.app(target=main)