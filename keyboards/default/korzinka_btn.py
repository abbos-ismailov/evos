from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tolov_bekor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Bekor qilish"),
            KeyboardButton(text="💰 To'lov qilish")
        ],
        [
            KeyboardButton(text="🔷 Asosiy menu")
        ]
    ],
    resize_keyboard=True
)

location_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Lokatsiya", request_location=True)
        ]
    ],
    resize_keyboard=True
)