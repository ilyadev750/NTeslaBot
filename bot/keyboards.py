from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

keyboard_1 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
button_1 = KeyboardButton(text='/arrivals')
button_2 = KeyboardButton(text='/departures')
keyboard_1.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
button_3 = KeyboardButton(text='/yesterday')
button_4 = KeyboardButton(text='/today')
button_5 = KeyboardButton(text='/tomorrow')
keyboard_2.add(button_3, button_4, button_5)