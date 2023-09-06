from aiogram import Bot, Dispatcher, executor, types


MY_TOKEN = "6542990215:AAErSHJUVLj2GEoheBrfyQ2WNrjssnLqZms"


bot = Bot(MY_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp)