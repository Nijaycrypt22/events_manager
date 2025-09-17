from nicegui import ui,app
from pages.home import *
from pages.create_event import * 
from pages.event import *
from pages.college import *
from pages.not_found import *
from pages.signin import *
from pages.signup import *
from components.navbar import *

app.add_static_files('/assets', 'assets')
ui.run()