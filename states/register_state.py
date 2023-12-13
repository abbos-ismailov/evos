from aiogram.dispatcher.filters.state import State, StatesGroup

class Registr(StatesGroup):
    full_name = State()
    phone_number = State()