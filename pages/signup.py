# from nicegui import ui
# from components.navbar import show_navbar
# from components.footer import show_footer

# @ui.page("/signup")
# def show_signup_page():
#     with ui.grid(columns=2).classes('h-screen w-full items-center justify-center'):
#         # Left side with welcome message and login button
#         with ui.column().classes("w-full h-screen bg-cover bg-center items-center justify-center flex").style("background-image:url(/assets/signup.png)"):
#             with ui.column().classes("text-center items-center bg-black/1 p-40"):
#                 ui.label("Welcome back").classes("text-white font-extrabold text-4xl")
#                 ui.label("To keep connected with us, give us your information").classes("text-white")
#                 ui.element("div").classes("")
#                 ui.button("login").classes("bg-grey")

#         # Right side with sign-up form
#         with ui.column().classes("w-full h-screen flex items-center justify-center"):
        
#             with ui.column().classes("w-[500px]"):  # Set a fixed width for better alignment
#                 ui.label("Sign Up to Event Hive").classes("text-xl font-bold mb-4")

#                 # Form fields
#                 ui.label("FIRST NAME")
#                 ui.input("enter your name").props("outlined").classes("w-full mb-2")
#                 ui.label("SURNAME")
#                 ui.input("enter your name").props("outlined").classes("w-full mb-2")
#                 ui.label("PASSWORD")
#                 ui.input("enter your password").props("outlined").classes("w-full mb-2")
#                 ui.label("CONFIRM PASSWORD")
#                 ui.input("confirm password").props("outlined").classes("w-full mb-4")

#                 ui.button("Sign UP", on_click=lambda: ui.notify("Sign Up clicked")).classes("w-full bg-purple")

#                 ui.label("or").classes("text-center w-full my-4")

#                 # Google Sign-up button
#                 def signup_with_google():
#                     ui.notify('Redirecting to Google sign-up...')

#                 with ui.button(on_click=signup_with_google).classes(
#                     'w-full bg-white text-gray-700 border border-gray-300 hover:bg-gray-100'
#                 ):
#                     with ui.row().classes('w-full items-center justify-center'):
#                         ui.image('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg').classes('w-6 h-6 mr-2')
#                         ui.label('Sign up with Google').classes('text-base font-medium text-black')
# from nicegui import ui

# @ui.page("/signup")
# def show_signup_page():
#     with ui.grid(columns=2).classes('w-full items-center justify-center'):
#         # Left side with welcome message and login button
#         with ui.column().classes("w-full h-screen bg-full bg-no-repeat bg-center items-center justify-center flex").style("background-image:url(/assets/signup.png)"):
#             with ui.column().classes("text-center items-center bg-black/1 p-40"):
#                 ui.label("Welcome back").classes("text-white font-extrabold text-4xl")
#                 ui.label("To keep connected with us, give us your information").classes("text-white text-lg")
#                 ui.element("div").classes("h-8") # A small spacer
#                 ui.button("signin").classes("bg-grey text-purple-600 font-semibold px-8 py-2 rounded-full")

#         # Right side with sign-up form
#         with ui.column().classes("w-full flex items-center justify-center"):
#             with ui.column().classes("w-[500px]"):
#                 ui.label("Event Hive").classes("text-4xl font-bold mb-4 text-purple-600")
#                 ui.label("Sign Up to Event Hive").classes("text-2xl font-bold mb-8")
                
#                 # Form fields with corrected labels
#                 ui.label("YOUR NAME").classes("text-sm font-semibold text-gray-700")
#                 ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")

#                 ui.label("YOUR NAME").classes("text-sm font-semibold text-gray-700")
#                 ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")

#                 ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
#                 ui.input(placeholder="Enter your password").props("outlined").classes("w-full mb-4")

#                 ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
#                 ui.input(placeholder="Confirm password").props("outlined").classes("w-full mb-8")
                
#                 # Sign-up button
#                 ui.button("Sign Up", on_click=lambda: ui.notify("Sign Up clicked")).classes("w-full bg-purple-600 text-white font-semibold py-2 rounded-full mb-4")
                
#                 # "Or" divider
#                 with ui.row().classes('w-full items-center my-4'):
#                     ui.element('div').classes('flex-grow h-[1px] bg-gray-300')
#                     ui.label('or').classes('text-gray-500 mx-4')
#                     ui.element('div').classes('flex-grow h-[1px] bg-gray-300')
                
#                 # Google Sign-up button
#                 def signup_with_google():
#                     ui.notify('Redirecting to Google sign-up...')

#                 with ui.button(on_click=signup_with_google).classes(
#                     'w-full bg-white text-gray-700 border border-gray-300 hover:bg-gray-100 py-2 rounded-full'
#                 ):
#                     with ui.row().classes('w-full items-center justify-center'):
#                         ui.image('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg').classes('w-6 h-6 mr-2')
#                         ui.label('Sign up with Google').classes('text-base text-black font-medium')
from nicegui import ui

@ui.page("/signup")
def show_signup_page():
    with ui.grid(columns=2).classes('w-full h-screen'):
        # Left side with welcome message and login button
        # Changed bg-full to bg-cover to make the image stretch
        with ui.column().classes("w-full h-screen bg-cover bg-no-repeat bg-center items-center justify-center flex").style("background-image:url(/assets/signup.png)"):
            with ui.column().classes("text-center items-center bg-black/1 p-40"):
                ui.label("Welcome back").classes("text-white font-extrabold text-4xl")
                ui.label("To keep connected with us, give us your information").classes("text-white text-lg")
                ui.element("div").classes("h-8") # A small spacer
                ui.button("signin").classes("bg-grey text-purple-600 font-semibold px-8 py-2 rounded-full")

        # Right side with sign-up form
        with ui.column().classes("w-full flex items-center justify-center"):
            with ui.column().classes("w-[500px]"):
                ui.label("Event Hive").classes("text-4xl font-bold mb-4 text-purple-600")
                ui.label("Sign Up to Event Hive").classes("text-2xl font-bold mb-8")
                
                # Form fields with corrected labels
                ui.label("YOUR NAME").classes("text-sm font-semibold text-gray-700")
                ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")

                ui.label("YOUR NAME").classes("text-sm font-semibold text-gray-700")
                ui.input(placeholder="Enter your name").props("outlined").classes("w-full mb-4")

                ui.label("PASSWORD").classes("text-sm font-semibold text-gray-700")
                ui.input(placeholder="Enter your password").props("outlined").classes("w-full mb-4")

                ui.label("CONFIRM PASSWORD").classes("text-sm font-semibold text-gray-700")
                ui.input(placeholder="Confirm password").props("outlined").classes("w-full mb-8")
                
                # Sign-up button
                ui.button("Sign Up", on_click=lambda: ui.notify("Sign Up clicked")).classes("w-full bg-purple-600 text-white font-semibold py-2 rounded-full mb-4")
                
                # "Or" divider
                with ui.row().classes('w-full items-center my-4'):
                    ui.element('div').classes('flex-grow h-[1px] bg-gray-300')
                    ui.label('or').classes('text-gray-500 mx-4')
                    ui.element('div').classes('flex-grow h-[1px] bg-gray-300')
                
                # Google Sign-up button
                def signup_with_google():
                    ui.notify('Redirecting to Google sign-up...')

                with ui.button(on_click=signup_with_google).classes(
                    'w-full bg-white text-gray-700 border border-gray-300 hover:bg-gray-100 py-2 rounded-full'
                ):
                    with ui.row().classes('w-full items-center justify-center'):
                        ui.image('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg').classes('w-6 h-6 mr-2')
                        ui.label('Sign up with Google').classes('text-base text-black font-medium')