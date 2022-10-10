from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

##bot = Bot(token=os.getenv('TOKEN'))
bot=Bot(token='5607198410:AAF_NQnCDSOlVG-A2G-2yPpMg-DKvEVTwWM')
dp = Dispatcher(bot, storage=storage)