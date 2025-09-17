from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/signin")
def show_signin_page():
    ui.label("welcome to the signin page")
