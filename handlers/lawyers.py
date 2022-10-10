from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class FSMLawer(StatesGroup):
    question = State()
    answer = State()
    dialog_id = State()
    assessment = State()

@dp.message_handler(comands = 'ЗАгрузить', state=None)
async def cm_start(message : types.Message):
    await FSMLawer.photo.set()
    await message.reply('Загрузи фото')