from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import keyboard_client

'''*********клиентская часть*********'''
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'С помощью бота вы можете получить ответ на любой вопрос от дипломированного юриста', reply_markup=keyboard_client)

async def command_question(message : types.Message):
    await bot.send_message(message.from_user.id, 'Напишите свой вопрос следующим сообщением')

async def command_assessment(message : types.Message):
    await bot.send_message(message.from_user.id, 'Оцените ответ на ваш вопрос')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_question, commands=['Задать_вопрос'])
    dp.register_message_handler(command_assessment, commands=['Оценка'])