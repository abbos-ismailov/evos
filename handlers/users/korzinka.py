from aiogram import types
from loader import dp, db, bot
from keyboards.default.korzinka_btn import tolov_bekor
from data.config import ADMINS
from keyboards.inline.inline_btns import show_foods_user
from keyboards.inline.foods_btn import foods_data_inline, buy_food_btn_func

@dp.message_handler(text="🛒 Savatcha")
async def savatcha(msg: types.Message):
    korzinka_foods = await db.show_korzinka(msg.from_user.id)
    
    if korzinka_foods:   
        text = ""
        albom = types.MediaGroup()
        for i in range(len(korzinka_foods)-1):
            albom.attach_photo(korzinka_foods[i][4])
            text += f"{i+1}.  <b>{korzinka_foods[i][2]}  {korzinka_foods[i][3]} so'm</b> {korzinka_foods[i][6]} ta\n"
        text += f"{len(korzinka_foods)}.  <b>{korzinka_foods[len(korzinka_foods)-1][2]}  {korzinka_foods[len(korzinka_foods)-1][3]} so'm</b> {korzinka_foods[len(korzinka_foods)-1][6]} ta"
        albom.attach_photo(korzinka_foods[len(korzinka_foods)-1][4], caption=text)
            
        await bot.send_media_group(chat_id=msg.from_user.id, media=albom)
        await msg.answer("To'lov qilamizmi!!!", reply_markup=tolov_bekor)

    else:
        await msg.answer("Savatchangiz bo'sh")
@dp.message_handler(text="❌ Bekor qilish")
async def clear_orders(msg: types.Message):
    await db.delete_korzinka(user_tg_id=msg.from_user.id)
    await msg.answer("Savatchangizdagi buyurtmalar tozalandi")
    