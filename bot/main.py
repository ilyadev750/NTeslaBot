from scraper.scraper import Parser
from keyboards import keyboard_1, keyboard_2
# from aiogram import Bot, Dispatcher, executor, types
from aiogram import executor
from aiogram import exceptions
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"
#
#
# bot = Bot(MY_TOKEN)
# dp = Dispatcher(bot)
#
#

#
#
# # @dp.message_handler(commands=['start'])
# # async def echo(message: types.Message, state: FSMContext):
# #     await message.answer(text=START_MESSAGE, reply_markup=keyboard_1)
#
#

from prepare_bot import dp
import dialog_with_user

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
