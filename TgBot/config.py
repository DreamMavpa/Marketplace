from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = 'token'
admin_id = 'admin_id'

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


