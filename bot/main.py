from aiogram import Bot, Dispatcher, executor, types
from scraper import Parser


MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"
START_MESSAGE = """Hello! Welcome to Nicola Tesla airport bot. You could get information about arrivals and departures. 
Please, choose the parameters"""


MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"


bot = Bot(MY_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text=START_MESSAGE)


if __name__ == '__main__':
    executor.start_polling(dp)
async def start(message: types.Message):
    await message.answer('<b>Welcome to Nicola Tesla Airport bot. You could get information about arrivals and '
                         'departures. Choose your options: </b>', parse_mode='HTML')


@dp.message_handler(commands=['arrivals'])
async def arrivals(message: types.Message):
    my_parser = Parser(type_of_schedule='Departures', day='Today')
    my_parser.run()
    await message.answer(f'{my_parser.all_flights[0]}')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('TEST WORK')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
