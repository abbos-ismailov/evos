from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.tolov_shablon import Product
from loader import db
from aiogram.types import LabeledPrice

# purchases_clothes = await db.show_purchases(user_tg_id=)
async def foods_pay(user_id):
    
    ordered_foods = await db.show_korzinka(user_tg_id=user_id)
    prices_list = []
    
    for pr in ordered_foods:
        prices_order_pr = await db.select_food_from_ordered_foods(pr['food_id'])
        pr_price = prices_order_pr['food_price']
        
        food_count = pr['food_count']
        food_name = pr['food_name']

        price_label = LabeledPrice(
                label=f"{food_name} => {pr_price} so'm * {food_count} ta   =",
                amount=food_count*int(pr_price)*100
            )
        prices_list.append(price_label)
    

    
    

    foods = Product(   
        title="To'lov qilish",
        description="Fast Food",
        currency="UZS",
        prices=prices_list,
        start_parameter="create_invoice_clothes",
        photo_url="https://cdn2.iconfinder.com/data/icons/transports-2/200/Untitled-9-1024.png",
        photo_width=1280,
        photo_height=564,
        need_name=True,
        need_phone_number=True,
        need_shipping_address=True,
        is_flexible=True
    )
    return foods



FAST_SHIPPING = types.ShippingOption(
    id='one_hour',
    title="1 soat ichida yetkaziladi",
    prices=[
        LabeledPrice("Maxsus sumka", 3_000_00),
        LabeledPrice("1 soat ichida yetkazish xizmati", 15_000_00),
    ]
)


REGULAR_SHIPPING = types.ShippingOption(
    id='one_half_hour',
    title="1.5 soat ichida yetkaziladi",
    prices=[
        LabeledPrice("Maxsus sumka", 3_000_00),
        LabeledPrice("1.5 soat ichida yetkazish xizmati", 10_000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='dokon',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Dastavkasiz", 0),
    ]
)