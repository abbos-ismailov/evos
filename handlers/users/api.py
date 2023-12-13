import requests
from loader import dp
from aiogram import types
from states.add_state import Weather
from aiogram.dispatcher import FSMContext

url = "https://api.openweathermap.org/data/2.5/"
key = "4d63db9c73dd0c0f45db68186b126447"




@dp.message_handler(text="🌦 Ob-Havo")
async def menu(msg: types.Message):
    await msg.answer("Qaysi joyni ob havosini bilmoqchisiz.")
    await Weather.weather.set()
    

@dp.message_handler(state=Weather.weather)
async def weather(msg: types.Message, state=FSMContext):
    response = requests.get(f"{url}weather?q={msg.text}&units=metric&APPID={key}")

    data = response.json()
    cod = data.get('cod')
    
    if cod == 200:
        weather_desc = data.get('weather')[0].get('description')
        weather_main = data.get('weather')[0].get('main')
        main_temp = data.get('main').get('temp')
        main_temp_min = data.get('main').get('temp_min')
        main_temp_max = data.get('main').get('temp_max')
        sys_country = data.get('sys').get('country')
        name = data.get('name')
        
        text = f"Name: <b>{name}</b>  Country: <b>{sys_country}</b>\nTemp: <b>{round(main_temp)}°C</b> Min_temp: <b>{round(main_temp_min)}°C</b>\n Max_temp: <b>{round(main_temp_max)}°C</b>"
        text += f"""\n<i>Description: <b>{weather_desc}</b></i>   <b>{weather_main}</b>"""
        await msg.answer(text)
        await state.finish()
    else:
        await msg.answer("Bunday Joy topa olmadik")