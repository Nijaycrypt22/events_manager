from nicegui import ui

def show_footer():

   with ui.column().classes("bg-blue-900 w-full h-[13rem] flex flex-col self-center"):
      with ui.row().classes('items-center text-center self-center'):
         ui.label("Event").classes("text-white text-2xl text-bol self-center")
         ui.label("Hive").classes("text-blue-800 text-2xl text-bold")
      with ui.row().classes("item-center self-center"):
          ui.input("enter your email").classes("bg-white self-center w-[20rem] rounded-lg").props("outlined dense")
          ui.button("subscribe").classes("self-center")
      with ui.row().classes(" items-center text-center flex self-center"):
         ui.link("Home").classes("text-white")
         ui.link("About").classes("text-white")
         ui.link("Services").classes("text-white")
         ui.link("Get in touch").classes("text-white")
         ui.link("FAQS").classes("text-white")
      ui.separator().classes("bg-white")
      

    # Copyright right, languages left, socials center
      with ui.row().classes('items-center w-full text-xs text-white'):
          with ui.row().classes('space-x-4 flex-1 justify-start'):
            ui.button('English')
            ui.label('French')
            ui.label("Hindi")
          with ui.row().classes('space-x-4 flex-1 justify-center'):
            ui.icon('img:https://cdn-icons-png.flaticon.com/512/174/174857.png').classes('w-6 h-6 hover:text-white')
            ui.icon('img:https://cdn-icons-png.flaticon.com/512/174/174883.png').classes('w-6 h-6 hover:text-white')
            ui.icon('img:https://cdn-icons-png.flaticon.com/512/25/25231.png').classes('w-6 h-6 hover:text-white')
          with ui.row().classes('flex-1 justify-end'):
            ui.label('Non Copyrighted ©️ 2025 Upload by Eventify').classes('text-right')
         
         