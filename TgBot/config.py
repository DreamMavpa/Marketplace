from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '6193122952:AAGwk9cb5qI-oX2MoQ4InDEzJ4KWy-8vpXw'
admin_id = '5999623896'

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


