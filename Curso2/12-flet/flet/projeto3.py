import flet as ft
from todo_app import TodoApp

def main(page: ft.Page):
    page.title="ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    page.add(TodoApp())
    
ft.app(target=main)