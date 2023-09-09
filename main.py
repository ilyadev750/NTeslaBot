from aiogram import Bot, Dispatcher, executor, types


MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"
START_MESSAGE = """Hello! Welcome to Nicola Tesla airport bot. You could get information about arrivals and departures. 
Please, choose the parameters"""

bot = Bot(MY_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text=START_MESSAGE)


if __name__ == '__main__':
    executor.start_polling(dp)