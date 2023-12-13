from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


show_foods = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌯 Lavashlar", callback_data="Lavashlar"),
            InlineKeyboardButton(text="🌭 Xot-Doglar", callback_data="Xot-Doglar")
        ],
        [
            InlineKeyboardButton(text="🍕 Pitsalar", callback_data="Pitsalar"),
            InlineKeyboardButton(text="🥤 Ichimliklar", callback_data="Ichimliklar")
        ],
        [
            InlineKeyboardButton(text="🥗 Salatlar", callback_data="Salatlar"),
            InlineKeyboardButton(text="🍔 Burgerlar", callback_data="Burgerlar")
        ]
    ]
)


show_foods_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌯 Lavashlar", callback_data="user:lavashlar"),
            InlineKeyboardButton(text="🌭 Xot-Doglar", callback_data="user:Xot-Doglar")
        ],
        [
            InlineKeyboardButton(text="🍕 Pitsalar", callback_data="user:pitsalar"),
            InlineKeyboardButton(text="🥤 Ichimliklar", callback_data="user:ichimliklar")
        ],
        [
            InlineKeyboardButton(text="🥗 Salatlar", callback_data="user:salatlar"),
            InlineKeyboardButton(text="🍔 Burgerlar", callback_data="user:burgerlar")
        ]
    ]
)