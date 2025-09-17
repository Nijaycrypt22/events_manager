from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/college")
def show_college_page():
    show_navbar()
    ui.label("welcome to the college page")
    show_footer()