from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

HELP_COMMANDS = """
/help - список команд
/start - начало работы с ботом
/description - описание бота
"""
DESCRIPTION = "этот бот пока ни хрена не умеет"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
kb = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text='batton1', url='https://t.me/zlobny_gnom47')
button2 = InlineKeyboardButton(text='button2', url='https://t.me/grabli_pitona')
kb.add(button1, button2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='полезные ссылки', reply_markup=kb)

    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMANDS)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=DESCRIPTION)


if __name__ == "__main__":
    executor.start_polling(dp)
