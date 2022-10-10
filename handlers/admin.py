from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSMAdmin(StatesGroup):
    question = State()
    answer = State()


@dp.message_handler(comands = 'ЗАгрузить', state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото')