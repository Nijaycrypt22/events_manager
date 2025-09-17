from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/")
def show_home_page():
    show_navbar()
    
    with ui.element("div").classes("h-screen w-screen flex flex-col relative bg-no-repeat bg-cover bg-center").style("background-image:url(/assets/event.png)"):
        with ui.column().classes("h-full w-full items-center justify-center text-center"):
            ui.label("Made For Those").classes("text-bold items-center self-center text-white uppercase").style("font-size:4rem;")
            ui.label("Who Do").classes("text-bold items-center self-center text-white uppercase").style("font-size: 4rem;")

    # Search bar section
    with ui.row().classes("bg-blue-900 p-4 no-gap items-center justify-center w-full max-w-screen-lg -mt-20 self-center rounded relative z-10"):
        with ui.column():
            ui.label("Looking for").classes("text-white text-semi-bold")
            ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")

        with ui.column():
            ui.label("Location").classes("text-white text-semi-bold")
            ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")
        
        with ui.column():
            ui.label("when").classes("text-white text-semi-bold")
            ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")
    
    # Main content container
    with ui.column().classes("w-full items-center"):
        # Upcoming Events section
        with ui.row().classes('w-full max-w-screen-lg mt-10 px-4 items-end justify-between'):
            with ui.row().classes("gap-x-2"):
                ui.label("Upcoming").classes('text-bold text-4xl')
                ui.label("Events").classes('text-bold text-blue-900 text-3xl')
            with ui.row().classes("gap-x-5"):
                ui.select(["Weekdays"]).classes("w-40 h-10 bg-white").props("outlined")
                ui.select(["Event type"]).classes("w-40 h-10 bg-white").props("outlined")
                ui.select(["Any Category"]).classes("w-40 h-10 bg-white").props("outlined")
        
        # Events grid
        with ui.grid(columns=3).classes("w-full max-w-screen-lg mt-5 gap-x-5 gap-y-5 px-4"):
            for i in range(6):
                with ui.card().classes("w-full h-[25rem] p-4"):
                    ui.label("event title")
                    ui.image("/assets/seller.png").classes("w-full")
                    ui.label("Bestseller Book Bootcamp-write, Market & Publish your books-Lucknow").classes('text-bold text-2xl')
                    ui.label("Sunday 16 November").classes("text-blue-900")
                    ui.label("online-event: join anywhere").classes('text-gray-700')
        ui.button("load more..").classes("self-center bg-blue-900 mt-10")

        # "Make Your Own Event" section - Corrected spacing
        with ui.column().classes("h-auto w-screen bg-blue-900 mt-20 p-4 items-center justify-center relative"):
            with ui.grid(columns=2).classes("w-full max-w-screen-lg items-center justify-center gap-x-10"):
                with ui.column().classes("relative -mt-20"):
                    ui.image("/assets/banner.png").classes("w-[400px]")
                with ui.column().classes("items-start justify-center text-white -ml-10"):  # Adjusted classes here
                    ui.label("Make Your Own Event").classes("font-bold text-3xl")
                    ui.label("You Can Create your Own event here").classes("text-xl font-light mt-2")
                    ui.button("Create Events", on_click=lambda: ui.navigate.to('http://127.0.0.1:8080/events')).classes("bg-purple-600 mt-5")

        # Brands section
        ui.image("/assets/Brand.png").classes("w-full max-w-screen-lg mt-20")

        # Blogs section
        with ui.row().classes("w-full max-w-screen-lg mt-10"):
            ui.label("Our").classes("text-2xl text-bold text-black")
            ui.label("Blogs").classes("text-blue-900 text-2xl text-bold ml-2")
        
        with ui.grid(columns=3).classes("w-full max-w-screen-lg mt-10 gap-x-5 gap-y-5"):
            with ui.card().classes("w-full h-[25rem]"):
                ui.image("/assets/seller.png").classes("w-full h-auto")
                ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow")
                ui.label("Saturdat, March 18, 9.30PM")
                ui.label("ONLINE EVENT - Attend anywhere")
            with ui.card().classes("w-full h-[25rem]"):
                ui.image("/assets/event2.png").classes("w-full h-auto")
                ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow")
                ui.label("Saturdat, March 18, 9.30PM")
                ui.label("ONLINE EVENT - Attend anywhere")
            with ui.card().classes("w-full h-[25rem]"):
                ui.image("/assets/seller.png").classes("w-full h-auto")
                ui.label("BestSelller Book Bootcamp -write, Market & Publish Your Book -Lucknow")
                ui.label("Saturdat, March 18, 9.30PM")
                ui.label("ONLINE EVENT - Attend anywhere")
                
    show_footer()