import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import configparser
import db as db
from datetime import datetime


config = configparser.ConfigParser()
config.read('config.ini', encoding="utf-8")
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config['settings']['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id == int(config['settings']['admin_id']):
        main_menu_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton('📃Добавить товар')
        button2 = KeyboardButton('👤Админ меню')
        main_menu_admin.add(button1, button2)
        await message.answer(f"Добро пожаловать, @{message.from_user.username}!", reply_markup=main_menu_admin)
    else:
        _Check = await db.checkUser(user_id = message.from_user.id, )
        if _Check == 1:
            print(config['settings']['admin_id'])
            main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = KeyboardButton('🖥️Купить дедик')
            button2 = KeyboardButton('🆘Помощь')
            button3 = KeyboardButton('👤Профиль')
            main_menu.add(button1, button2)
            main_menu.add(button3)
            await message.answer(f"Добро пожаловать, @{message.from_user.username} в магазин дедиков!", reply_markup=main_menu)
        else:
            now = datetime.now()
            await db.insertUser(user_id=message.from_user.id, user_name = message.from_user.username, balance = 0, date = now, number_of_purch = 0)
            await message.answer(f"Добро пожаловать, @{message.from_user.username} в магазин дедиков!", reply_markup=main_menu)


async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())