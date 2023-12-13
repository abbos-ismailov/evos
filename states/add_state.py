from aiogram.dispatcher.filters.state import State, StatesGroup

class AddFood(StatesGroup):
    food_name = State()
    food_type = State()
    food_price = State()
    food_img = State()


class Delete(StatesGroup):
    food_id = State()

class Delete_Customer(StatesGroup):
    user_id = State()

class Weather(StatesGroup):
    weather = State()