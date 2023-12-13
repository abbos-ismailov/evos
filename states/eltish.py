from aiogram.dispatcher.filters.state import State, StatesGroup

class Yetkazish(StatesGroup):
    phone_number = State()
    location = State()
    orintir = State()