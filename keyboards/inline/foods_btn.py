from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def foods_data_inline(data):
    show_foods = InlineKeyboardMarkup(row_width=2)
    back_foods_types = InlineKeyboardButton(text="↩ Orqaga", callback_data="foods_types")
    
    for i in data:
        show_foods.insert(InlineKeyboardButton(text=i['food_name'], callback_data=f"foods:{i['food_id']}"))

    show_foods.insert(back_foods_types)
    return show_foods


def buy_food_btn_func(count, food_id, food_type):  
    buy_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="ayirish"),
                InlineKeyboardButton(text=count, callback_data="count_show"),
                InlineKeyboardButton(text="➕", callback_data="qoshish"),
            ],
            [
                InlineKeyboardButton(text="🛒 Savatchaga", callback_data=f"bought_food:{food_id}:{food_type}")
            ],
            [
                InlineKeyboardButton(text="↩ Orqaga", callback_data=f"back_foods_type_show:{food_type}")
            ]
        ]
    )
    return buy_btn
