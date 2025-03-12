import flet as ft
from task import Task

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(
            hint_text="O que precisa ser feito?",
            on_submit=self.add_clicked, expand=True
        )
        self.tasks = ft.Column()
        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="all"),
                ft.Tab(text="active"),
                ft.Tab(text="completed"),
            ]
        )
        self.items_left = ft.Text("0 items left")
        self.width = 600
        self.controls = [
            ft.Row(
                [ft.Text(value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD,
                        on_click=self.add_clicked
                    )
                ]
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Limpar tarefas concluídas",
                                on_click=self.clear_clicked
                            )
                        ]
                    )
                ]
            )
        ]
    def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update()
            
    def task_status_change(self, task):
        self.update()
        
    def tabs_changed(self, task):
        self.update()
        
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()
    
    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)
                
    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and not task.completed)
                or (status == "completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"