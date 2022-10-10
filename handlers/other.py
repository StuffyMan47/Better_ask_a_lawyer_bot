from aiogram import types, Dispatcher
from create_bot import dp, bot

async def send_pidor(message: types.Message):
    await bot.send_message(message.from_user.id, "принял текст вопроса")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(send_pidor)
