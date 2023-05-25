from aiogram import *
from config import *
from KeyboardMarkup.ReplyKeyboardMarkup import *
from inlinekey.InlineKeyBoard import *
import sqlite3
from sqlite3 import Error
from Main_function.Edit_Folder import *
import os
import sys
from Main_function.State_group import *
sys.path.insert(1,os.path.abspath('../Marketplace/'))
from DB.db import init_db,add_message_shop_list_table,add_message_shop_list_tooling,read_sqlite_table,check_db_product_name
from aiogram.dispatcher.filters import Text


bot = Bot(token)






inline_callback_cheker = False
btn_del_inlinekeyboard = False
#//////////////////////////////////////////////////////////////////////////////////////////// Удаление товаров начало
# @dp.message_handler(text='Удалить объявления')
async def db_drop(message: types.Message):
    msg = str(message.from_id)
    # try:
    if admin_id == msg:
        global btn_del_inlinekeyboard
        
        if btn_del_inlinekeyboard != False:
            await btn_del_inlinekeyboard.delete()
        

        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Меню удаление",reply_markup=inline_menu_delete_product)
        
    
        
    else:
        await bot.send_message(msg,"Вы не админ,у вас нет прав доступа!")
    # except:
    #     await bot.send_message(msg,"Перезапустите бота /start!")







#filter for delet
# @dp.callback_query_handler(lambda c: c.data == 'button_del_focus')
async def process_callback_button_del_focus(callback_query: types.CallbackQuery):


    global btn_del_inlinekeyboard
    await btn_del_inlinekeyboard.delete()
    btn_del_inlinekeyboard = await bot.send_message(admin_id,".",reply_markup=product_btn_group_del_call)









# @dp.callback_query_handler(lambda c: c.data == 'tooling_del')
async def process_callback_tooling_del(callback_query: types.CallbackQuery):
    global db_name_btn
    db_name_btn = 'shop_list_tooling'

    global inline_callback_cheker
    inline_callback_cheker = 'tooling_del'

    global btn_del_inlinekeyboard

    if len(chek_db_telegram('shop_list_tooling')[1])>0:
        chek_db_telegram('shop_list_tooling')
        await bot.answer_callback_query(callback_query.id)
        
        
        await btn_del_inlinekeyboard.delete()
    

        
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('shop_list_tooling')[0]), reply_markup=catalog_menu_btn_del('shop_list_tooling'))
     
   
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")







# @dp.callback_query_handler(lambda c: c.data == 'table_del')
async def process_callback_table_del(callback_query: types.CallbackQuery):
    global db_name_btn
    db_name_btn = 'shop_list_table'

    global inline_callback_cheker
    inline_callback_cheker = 'table_del'

    global btn_del_inlinekeyboard

    if len(chek_db_telegram('shop_list_table')[1])>0:
        chek_db_telegram('shop_list_table')
        await bot.answer_callback_query(callback_query.id)

        
        await btn_del_inlinekeyboard.delete()
    

        
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('shop_list_table')[0]), reply_markup=catalog_menu_btn_del('shop_list_table'))
       
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")





# @dp.callback_query_handler(lambda c: c.data == 'other_products_del')
async def process_callback_other_products_del(callback_query: types.CallbackQuery):
    global db_name_btn
    db_name_btn = 'other_products_list'

    global inline_callback_cheker
    inline_callback_cheker = 'other_products_del'

    global btn_del_inlinekeyboard

    if len(chek_db_telegram('other_products_list')[1])>0:
        chek_db_telegram('other_products_list')
        await bot.answer_callback_query(callback_query.id)

        
        await btn_del_inlinekeyboard.delete()
    

        
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('other_products_list')[0]), reply_markup=catalog_menu_btn_del('other_products_list'))
       
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")









# @dp.callback_query_handler(lambda c: c.data == 'button_del_full_db')
async def process_callback_button_del_full_db(callback_query: types.CallbackQuery):
    drop_db()
    init_db()
    drop_img()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(admin_id,"База данных очищена")
    print("База данных очищена")





#//////////////////////////////////////////////////////////////////////////////////////////// Удаление товаров конец





# @dp.callback_query_handler(lambda c: c.data == 'product_delete_')
async def callback_check(callback_query: types.CallbackQuery):

    x = callback_query.data
    global inline_callback_cheker
    global btn_del_inlinekeyboard
    

    
    match inline_callback_cheker:
        case 'other_products_del':
       
            check_id = ''
            for i in x[15:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('other_products_list',check_id)

            focus_del_item_pos(id_generator_del(id_generator_del(x[15:])),'other_products_list')
            focus_del_img_folder(name_folder_generator_del(id_generator_del(x[15:])),'other_products_list')

            await btn_del_inlinekeyboard.delete()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы удалили: '+str(pd_name)) 

        case 'table_del':
            
            check_id = ''
            for i in x[15:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('shop_list_table',check_id)

            focus_del_item_pos(id_generator_del(id_generator_del(x[15:])),'shop_list_table')
            focus_del_img_folder(name_folder_generator_del(id_generator_del(x[15:])),'shop_list_table')

            await btn_del_inlinekeyboard.delete()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы удалили: '+str(pd_name)) 

        case 'tooling_del':
            
            check_id = ''
            for i in x[15:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('shop_list_tooling',check_id)

            focus_del_item_pos(id_generator_del(id_generator_del(x[15:])),'shop_list_tooling')
            focus_del_img_folder(name_folder_generator_del(id_generator_del(x[15:])),'shop_list_tooling')

            await btn_del_inlinekeyboard.delete()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы удалили: '+str(pd_name)) 




#////////////////////////////////////////////////////////////////////////////////////////// Скрол страниц начало удаления

btn_counter = 0

# @dp.callback_query_handler(lambda c: c.data == 'btn_next_del')
async def btn_del_next(callback_query: types.CallbackQuery):
    global db_name_btn

    count_upper = 1
    global btn_counter

    btn_counter = catalog_menu_all_btn_del(btn_counter,db_name_btn)[1] + count_upper

    global btn_del_inlinekeyboard
    await btn_del_inlinekeyboard.delete()
    

    
    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_del(btn_counter,db_name_btn)[0])
    



# @dp.callback_query_handler(lambda c: c.data == 'btn_back_del')
async def btn_del_back(callback_query: types.CallbackQuery):
    count_upper = 1
    global btn_counter
    global btn_del_inlinekeyboard
    # await btn_del_inlinekeyboard.delete()
    btn_counter = catalog_menu_all_btn_del(btn_counter,db_name_btn)[1] - count_upper
    
    if btn_counter < 0:
        btn_counter = 0

        await btn_del_inlinekeyboard.delete()
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_del(btn_counter,db_name_btn)[0])
    else:

        await btn_del_inlinekeyboard.delete()
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_del(btn_counter,db_name_btn)[0])



#////////////////////////////////////////////////////////////////////////////////////////// Скрол страниц конец удаления












def reg_handler_remove(dp: Dispatcher):

    #Удаление товаров выбор
    dp.register_message_handler(db_drop,text='Удалить объявления')

    dp.register_callback_query_handler(process_callback_button_del_focus, lambda c: c.data == 'button_del_focus')

    dp.register_callback_query_handler(process_callback_tooling_del, lambda c: c.data == 'tooling_del')

    dp.register_callback_query_handler(process_callback_table_del, lambda c: c.data == 'table_del')

    dp.register_callback_query_handler(process_callback_other_products_del, lambda c: c.data == 'other_products_del')

    dp.register_callback_query_handler(process_callback_button_del_full_db, lambda c: c.data == 'button_del_full_db')


    
    #Скрол страниц
    dp.register_callback_query_handler(btn_del_next, lambda c: c.data == 'btn_next_del')

    dp.register_callback_query_handler(btn_del_back, lambda c: c.data == 'btn_back_del')


    #Callback check
    dp.register_callback_query_handler(callback_check, text_startswith='product_delete_')