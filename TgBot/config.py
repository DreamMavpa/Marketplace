from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '6109199062:AAHRLz-WqjvD7usbC9zPnZRIlPTm0f1lHJs'
admin_id = '5999623896'

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


