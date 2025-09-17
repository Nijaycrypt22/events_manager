from nicegui import ui
from components.navbar import show_navbar

@ui.page("/create_event")
def show_create_event_page():
    show_navbar()
    title=ui.input()