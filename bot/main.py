from aiogram import executor


from prepare_bot import dp
import dialog_with_user

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
