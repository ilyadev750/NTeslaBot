from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)


keyboard_1 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
button_1 = KeyboardButton(text='/arrivals')
button_2 = KeyboardButton(text='/departures')
keyboard_1.add(button_1, button_2)

keyboard_2 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
button_3 = KeyboardButton(text='Yesterday')
button_4 = KeyboardButton(text='Today')
button_5 = KeyboardButton(text='Tomorrow')
keyboard_2.add(button_3, button_4, button_5)

keyboard_3 = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
button_6 = KeyboardButton(text='/start')
keyboard_3.add(button_6)