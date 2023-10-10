from aiogram import Bot, Dispatcher, executor, types


MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"


bot = Bot(MY_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer('<b>Welcome to Nicola Tesla Airport bot. You could get information about arrivals and '
                         'departures. Choose your options: </b>', parse_mode='HTML')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('TEST WORK')

if __name__ == '__main__':
    executor.start_polling(dp)
    