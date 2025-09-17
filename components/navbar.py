from nicegui import ui


def show_navbar():
    with ui.row().classes(" w-full max-w-6xl mx-auto items-center justify-between p-16"):
        with ui.row():
             ui.label("Event").classes("text-bold text-2xl text-black")
             ui.label("Hive").classes("text-blue-900 text-bold text-2xl")
        with ui.row():
            ui.link('Login').classes("item-left")
            ui.button("Signup", on_click=lambda:ui.navigate.to('http://127.0.0.1:8080/signup')).props("outlined dense")