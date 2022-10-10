from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv
from create_bot import dp, bot

load_dotenv(find_dotenv())

async def on_startup(_):
    await bot.send_message('714862316', 'Бот начал работу')

from handlers import client, admin, other

client.register_handlers_client(dp)
#admin.register_handlers_
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
