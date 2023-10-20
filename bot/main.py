from scraper.scraper import Parser
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram import exceptions

MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"
START_MESSAGE = """Hello! Welcome to Nicola Tesla airport bot. You could get information about arrivals and departures. 
Please, choose the parameters"""
DAY = None

MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"

bot = Bot(MY_TOKEN)
dp = Dispatcher(bot)

keyboard_1 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
button_1 = KeyboardButton(text='/arrivals')
button_2 = KeyboardButton(text='/departures')
keyboard_1.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
button_3 = KeyboardButton(text='/yesterday')
button_4 = KeyboardButton(text='/today')
button_5 = KeyboardButton(text='/tomorrow')
keyboard_2.add(button_3, button_4, button_5)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text=START_MESSAGE, reply_markup=keyboard_1)


@dp.message_handler(commands=['departures'])
async def departures(message: types.Message):
    await message.answer('Please, choose the day:', reply_markup=keyboard_2)
    # my_parser = Parser(type_of_schedule='Departures', day='Today')
    # my_parser.run()
    # await message.answer(f'{my_parser.all_flights[0]}')


@dp.message_handler(commands=['today'])
async def today_arrivals(message: types.Message):
    my_parser = Parser(type_of_schedule='Departures', day='Today')
    my_parser.run()
    for flight in my_parser.list_of_flights:
        await message.answer(f'{flight}')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('TEST WORK')


@dp.errors_handler(exception=exceptions.RetryAfter)
async def exception_handler(update: types.Update, exception: exceptions.RetryAfter):
    # Do something
    return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
