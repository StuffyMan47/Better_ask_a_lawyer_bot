from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Задать_вопрос')
button2 = KeyboardButton('/help')
keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_client.row(button1, button2)
