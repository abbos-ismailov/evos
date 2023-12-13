from aiogram import types
from loader import dp, db
from aiogram.dispatcher.filters import Command
from keyboards.default.btns import admin_btn, food_btn, menu_btn
from keyboards.inline.inline_btns import show_foods
from data.config import ADMINS
from states.add_state import AddFood, Delete, Delete_Customer
from aiogram.dispatcher import FSMContext

@dp.message_handler(Command("menu"))
async def menu(msg: types.Message):
    await msg.answer("Menu dan Ovqatlar yoki Xaridlarni tanlashingiz mumkin", reply_markup=menu_btn)

@dp.message_handler(Command("admin_panel", prefixes="?/@"))
async def welcome_admin(msg: types.Message):
    await msg.answer("Admin Panelga hush kelibsiz", reply_markup=admin_btn)

### Asosiy menuga tushirish
@dp.message_handler(text="🔷 Asosiy menu")
async def main_menu(msg: types.Message):
    await msg.answer("Menyudan Ovqatlar yoki Savatchadagi mahsulotlarni ko'rishingiz mumkin", reply_markup=menu_btn)


### MAXSULOT QO"SHISH
@dp.message_handler(text="➕ Maxsulot qo'shish", user_id=ADMINS)
async def add_food(msg: types.Message):
    await msg.answer("Mahsulot nomini kiriting", reply_markup=types.ReplyKeyboardRemove())
    await AddFood.food_name.set()
    
@dp.message_handler(state=AddFood.food_name)   
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(
        {f"food_name": msg.text}
    )
    await msg.answer("Mahsulot narxini kiriting")
    await AddFood.food_price.set()

@dp.message_handler(state=AddFood.food_price)   
async def get_full_price(msg: types.Message, state: FSMContext):
    await state.update_data(
        {f"food_price": msg.text}
    )
    await msg.answer("Mahsulot turini kiriting", reply_markup=food_btn)
    await AddFood.food_type.set()

@dp.message_handler(state=AddFood.food_type)   
async def get_full_type(msg: types.Message, state: FSMContext):
    food_type_list = msg.text.split(" ")
    await state.update_data(
        {f"food_type": food_type_list[1]}
    )
    await msg.answer("Mahsulot rasmini tashlang", reply_markup=types.ReplyKeyboardRemove())
    await AddFood.food_img.set()

@dp.message_handler(state=AddFood.food_img, content_types=types.ContentType.PHOTO)   
async def get_full_img(msg: types.Message, state: FSMContext):
    await msg.answer(msg.photo[-1].file_id)
    
    data = await state.get_data()
    food_name = data.get('food_name')
    food_price = data.get('food_price')
    food_type = data.get('food_type')
    
    await db.add_food(food_name, food_price, msg.photo[-1].file_id, food_type)
    await msg.answer("Rahmat! Mahsulot bazaga saqlandi", reply_markup=admin_btn)
    await state.finish()

### DELETE FOOD function
@dp.message_handler(text="❌ Maxsulot o'chirish", user_id=ADMINS)
async def get_food_id_for_delete(msg: types.Message):
    await msg.answer("Mahsulot id sini tashlang")
    await Delete.food_id.set()

@dp.message_handler(state=Delete.food_id)
async def delete_food(msg: types.Message, state: FSMContext):
    try:
        await db.delete_food(int(msg.text))
    except Exception as e:
        await msg.answer("Mahsulot ID si faqat raqam qabul qiladi")
        return
    await msg.answer("Mahsulot ochib ketdi")
    await state.finish()


### SHOW FOODS function
###----------------------- Functionni kamaytirish kerak
@dp.message_handler(text="👀 Maxsulotlarni ko'rish", user_id=ADMINS)
async def show_foods_func(msg: types.Message):
    await msg.answer("Qaysi turdagi mahsulotlarni ko'rmoqchisiz", reply_markup=show_foods)

@dp.callback_query_handler(text="Lavashlar", user_id=ADMINS)
async def show_lavashes_func(msg: types.CallbackQuery):
    foods_data = await db.show_foods(food_type="Lavashlar")

    for i in foods_data:
        await msg.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.callback_query_handler(text="Xot-Doglar", user_id=ADMINS)
async def show_xotdogs_func(msg: types.CallbackQuery):
    foods_data = await db.show_foods(food_type="Xot-Doglar")

    for i in foods_data:
        await msg.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.callback_query_handler(text="Pitsalar", user_id=ADMINS)
async def show_pizzas_func(msg: types.CallbackQuery):
    foods_data = await db.show_foods(food_type="Pitsalar")

    for i in foods_data:
        await msg.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.callback_query_handler(text="Ichimliklar", user_id=ADMINS)
async def show_liques_func(msg: types.CallbackQuery):
    foods_data = await db.show_foods(food_type="Ichimliklar")

    for i in foods_data:
        await msg.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.callback_query_handler(text="Salatlar", user_id=ADMINS)
async def show_salads_func(call: types.CallbackQuery):
    foods_data = await db.show_foods(food_type=call.data)

    for i in foods_data:
        await call.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.callback_query_handler(text="Burgerlar", user_id=ADMINS)
async def show_burgers_func(call: types.CallbackQuery):
    foods_data = await db.show_foods(food_type="Burgerlar")
    
    for i in foods_data:
        await call.message.answer(f"{i['food_name'].title()}  <b>{i['food_price']}</b> so'm --- ID: <b>{i['food_id']}</b>")

@dp.message_handler(text="🙍‍♂️ Buyurtmachilar")
async def customers(msg: types.Message):
    customers_list = await db.show_customers()
    if customers_list:
        for i in customers_list:
            text = f"<a href='https://t.me/{i[1]}'>{i[2]}</a> Tel: <b>{i[3]}</b> Lokatsiya: <b>{i[4]}</b> Orintir: {i[5]} Telegram ID: <code>{i[0]}</code>\n"
            await msg.answer(text)
    else:
       await msg.answer("Buyurtmachilar yo'q")

@dp.message_handler(text="❌ Buyurtmachilarni o'chirish", user_id=ADMINS)
async def delete_customer(msg: types.Message):
    await msg.answer("Buyurtmachi Telegram ID sini tashlang")
    await Delete_Customer.user_id.set()
    
@dp.message_handler(state=Delete_Customer.user_id, user_id=ADMINS)
async def delete_customer(msg: types.Message, state: FSMContext):
    await db.delete_customer(int(msg.text))
    await msg.reply("Bu buyurtmachi o'chib ketdi")
    await state.finish()