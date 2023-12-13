from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.register_state import Registr
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp, db
from keyboards.default.btns import menu_btn, menu_btn_en
from keyboards.inline.language import choice_lang



@dp.message_handler(Command('language'))
async def choose_lang(msg: types.Message):
    await msg.answer("Tilni tanlashingiz mumkin", reply_markup=choice_lang)
    print(msg)

@dp.callback_query_handler(text = "eng")
async def eng(call: types.CallbackQuery):
    await call.message.answer("you ara at main menu", reply_markup=menu_btn_en)

@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f"Salom, {msg.from_user.full_name} !\n/language commandasi orqali tilni tanlshiz mumkin")
    
    user_if_member = await db.get_one_user(user_tg_id=int(msg.from_user.id))
    
    if user_if_member == None:
        await msg.answer("Ro'yhatdan o'tish uchun. Ismingizni kiriting")
        await Registr.full_name.set()
    else:
        await msg.answer("Buyurtma beramizmi!!!", reply_markup=menu_btn)

@dp.message_handler(state=Registr.full_name)   
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(
        {f"full_name": msg.text}
    )
    await msg.answer("Telefon raqamingizni kiriting")
    await Registr.phone_number.set()

@dp.message_handler(state=Registr.phone_number)
async def get_phone_number(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_number": msg.text}
    )
    
    
    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    
    await state.finish()
    await db.add_user(msg.from_user.id, full_name, phone_number, msg.from_user.username)
    
    await msg.answer("Raxmat! Ro'yhatdan o'tdingiz. /menu Komandasi orqali siz Asosiy menu ga o'tishingiz mumkin", reply_markup=menu_btn)