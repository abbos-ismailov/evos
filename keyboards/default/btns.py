from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛 Ovqatlar"),
            KeyboardButton(text="🛒 Savatcha")
            # KeyboardButton(text="🌦 Ob-Havo")
        ]
    ],
    resize_keyboard=True
)

menu_btn_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍛 Foods"),
            KeyboardButton(text="🛒 Shopping cart")
            # KeyboardButton(text="🌦 Ob-Havo")
        ]
    ],
    resize_keyboard=True
)

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Maxsulot qo'shish"),
            KeyboardButton(text="❌ Maxsulot o'chirish"),
        ],
        [
            KeyboardButton(text="👀 Maxsulotlarni ko'rish"),
            KeyboardButton(text="🔷 Asosiy menu")
        ],
        [
            KeyboardButton(text="🙍‍♂️ Buyurtmachilar"),
            KeyboardButton(text="❌ Buyurtmachilarni o'chirish")
        ]
    ],
    resize_keyboard=True
)

food_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌯 Lavashlar"),
            KeyboardButton(text="🌭 Xot-Doglar"),
            KeyboardButton(text="🍕 Pitsalar")
        ],
        [
            KeyboardButton(text="🥤 Ichimliklar"),
            KeyboardButton(text="🥗 Salatlar"),
            KeyboardButton(text="🍔 Burgerlar")
        ]
    ],
    resize_keyboard=True
)