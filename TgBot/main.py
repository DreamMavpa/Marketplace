from aiogram import *
from config import *
from KeyboardMarkup.ReplyKeyboardMarkup import *
from inlinekey.InlineKeyBoard import *
from Main_function.Edit_Folder import *
import os
import sys
sys.path.insert(1,os.path.abspath('../laserbit/'))
from DB.db import init_db,read_sqlite_table


bot = Bot(token)



#///////////////////////////////////////////////////////////  КНОПКА ОТМЕНЫ НАЧАЛО
cancellation_buttons = ['Отмена']
keyboard_cancellation = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_cancellation.add(*cancellation_buttons)
#///////////////////////////////////////////////////////////  КНОПКА ОТМЕНЫ КОНЕЦ




init_db() #db creat and conect



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message,):
    global btn_del_inlinekeyboard
    btn_del_inlinekeyboard =  message
    msg = str(message.from_id)
    if admin_id == msg:
        await bot.send_message(msg,"Привет!", reply_markup=menu_frep())
    else:
        await bot.send_message(msg,"Вы не админ,у вас нет прав доступа!")






@dp.message_handler(text='Просмотреть активные объявления')
async def shop_check(message: types.Message):
    global btn_del_inlinekeyboard

    numb_colums_tooling = read_sqlite_table('id','shop_list_tooling')
    numb_colums_table = read_sqlite_table('id','shop_list_table')
    numb_colums_other = read_sqlite_table('id','other_products_list')
    summ_db = int(numb_colums_tooling) + int(numb_colums_table)+int(numb_colums_other)

    btn_del_inlinekeyboard = await message.reply(f'''Активных {str(summ_db)} объявлений
            
оснастка = {numb_colums_tooling}
столов = {numb_colums_table}
прочее = {numb_colums_other}

Выберите какой товар вы хотите добавить''', reply_markup=product_btn_group)
    
   


#Добавление товаров
from Main_function import add_handlers

add_handlers.reg_handler_add(dp)



#УДАЛЕНИЕ ТОВАРОВ

from Main_function import remove_handlers

remove_handlers.reg_handler_remove(dp)



#Редактирование товаров
from Main_function import edit_handlers

edit_handlers.reg_handler_edit(dp)




    







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

