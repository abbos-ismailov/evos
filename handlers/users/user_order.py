from aiogram import types
from aiogram.types import InputMediaPhoto
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.inline_btns import show_foods_user
from keyboards.inline.foods_btn import foods_data_inline, buy_food_btn_func
from handlers.users.foods_sort import foods_sort


@dp.message_handler(content_types=types.ContentType.PHOTO, user_id=ADMINS)
async def photo_id(msg: types.Message):
    await msg.answer(f"<code>{msg.photo[-1].file_id}</code>")

### Ovqatlar bolimini tanlaganda barcha ovqatlarni korsatdik
@dp.message_handler(text="🍛 Ovqatlar")
async def offer_food(msg: types.Message):
    photo_id = "AgACAgQAAxkBAAIB4GUEfuSMiTgpWdYAAXt1RLptSzKIbwACb68xG4_dlVBfICF9JkksFgEAAwIAA3gAAzAE"
    await msg.answer_photo(photo_id, caption="Qanday ovqat buyurtma qilmoqchisiz ?", reply_markup=show_foods_user)

### Back to foods types
@dp.callback_query_handler(text="foods_types")
async def lavash_func(call: types.CallbackQuery):
    await call.message.delete()
    photo_id = "AgACAgQAAxkBAAIB4GUEfuSMiTgpWdYAAXt1RLptSzKIbwACb68xG4_dlVBfICF9JkksFgEAAwIAA3gAAzAE"
    await call.message.answer_photo(photo_id, caption="Qanday ovqat buyurtma qilmoqchisiz ?", reply_markup=show_foods_user)


### Bir turdagi foodni tanlaganda shularni chiqardik
@dp.callback_query_handler(lambda c : c.data.startswith("user"))
async def lavash_func(call: types.CallbackQuery):
    await call.message.delete()
    food_type = call.data.split(":")[1].title()
    foods_data = await db.show_foods(food_type)
    
    food_list = foods_sort(food_type) ### Foods sorted
    photo_id = food_list[0]
    food_type_new = food_list[1]
    
    await call.message.answer_photo(photo=photo_id, caption=food_type_new, reply_markup=foods_data_inline(foods_data))


### Qaysidur ovqatni tanlaganda shuni malumotlarini chiqarib berdilk
@dp.callback_query_handler(lambda c: c.data.startswith("foods"))
async def one_lavash(call: types.CallbackQuery):
    choosen_food = await db.get_one_food(food_id=int(call.data.split(":")[1]))
    await call.message.delete()

    text = f"<b>{choosen_food[1]}</b> \nNarxi: <b>{choosen_food[2]} so'm</b>"
    await call.message.answer_photo(choosen_food[3], caption=text, reply_markup=buy_food_btn_func(1, int(call.data.split(":")[1]), choosen_food[4]))

### Orqaga ni boganda qaysi ovqatni tanlagan bolsa shunga qaytardik
@dp.callback_query_handler(lambda c: c.data.startswith("back_foods_type_show"))
async def back_to_foods_type(call: types.CallbackQuery):
    await call.message.delete()
    food_type = call.data.split(":")[1]
    foods = await db.show_foods(food_type)
    
    food_list = foods_sort(food_type) ### Tepadagi ish bilan bir xil boldi
    food_id = food_list[0]
    food_type_new = food_list[1]
    await call.message.answer_photo(food_id, caption=food_type_new, reply_markup=foods_data_inline(foods))


### Qoshish tugmasini bosganda edit qildik
@dp.callback_query_handler(text="qoshish")
async def add_one(call: types.CallbackQuery):
    food_id = int(call.message.reply_markup.inline_keyboard[1][0]["callback_data"].split(":")[1])
    food_type = call.message.reply_markup.inline_keyboard[1][0]["callback_data"].split(":")[2]
    count = int(call.message.reply_markup.inline_keyboard[0][1]["text"])  
    count += 1
    
    await call.message.edit_reply_markup(reply_markup=buy_food_btn_func(count, food_id, food_type))
    
    
@dp.callback_query_handler(text="ayirish")
async def add_one(call: types.CallbackQuery):
    food_id = int(call.message.reply_markup.inline_keyboard[1][0]["callback_data"].split(":")[1])
    food_type = call.message.reply_markup.inline_keyboard[1][0]["callback_data"].split(":")[2]
    count = int(call.message.reply_markup.inline_keyboard[0][1]["text"])  
    
    if count > 1:
        count -= 1
    else:
        return
    await call.message.edit_reply_markup(reply_markup=buy_food_btn_func(count, food_id, food_type))


@dp.callback_query_handler(lambda c: c.data.startswith("bought_food"))
async def add_ordered_foods(call: types.CallbackQuery):
    try:
        food_id = int(call.data.split(":")[1])
        food_type = call.data.split(":")[2]
        food_name = call.message.caption.split("\n")[0].strip()
        food_price = call.message.caption.split("\n")[1].split(" ")[1]
        food_count = int(call.message.reply_markup.inline_keyboard[0][1].text)
        
        await db.insert_food_to_orders(call.from_user.id, food_id, food_name, food_price, call.message.photo[-1].file_id, food_type, food_count)
        await call.message.answer(f"🛒   <b>{food_name} - {food_count} ta </b>  Savatchaga tushdi")
    except:
        print("Ma'luomot kelmay qoldi")