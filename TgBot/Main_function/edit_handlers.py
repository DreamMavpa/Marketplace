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
sys.path.insert(1,os.path.abspath('../laserbit/'))
from DB.db import init_db,add_message_shop_list_table,add_message_shop_list_tooling,read_sqlite_table,check_db_product_name
from aiogram.dispatcher.filters import Text

bot = Bot(token)







#//////////////////////////////////////////////////////////////////////////////////////////// Редактирование товаров
inline_callback_cheker = False
btn_del_inlinekeyboard = False

btn_counter = 0
# @dp.message_handler(text='Редактировать объявления')
async def edit_product(message: types.Message):
    msg = str(message.from_id)
    global btn_del_inlinekeyboard
    # try:
        
    if admin_id == msg:

        if btn_del_inlinekeyboard != False:
            await btn_del_inlinekeyboard.delete()    
            
        btn_del_inlinekeyboard = await bot.send_message(admin_id,'Меню редактирования', reply_markup=product_btn_group_edit_call)#редактирую здесь была функция catalog_menu()
    
            
       
    else:
        await bot.send_message(msg,"Вы не админ,у вас нет прав доступа!")
    # except:
    #     await bot.send_message(msg,"Перезапустите бота /start!")






# @dp.callback_query_handler(lambda c: c.data == 'tooling_edit')
async def edit_btn_tooling(callback_query: types.CallbackQuery):
    global db_name_btn
    db_name_btn = 'shop_list_tooling'
    global btn_del_inlinekeyboard
    if len(chek_db_telegram('shop_list_tooling')[1])>0:
                
                
                await btn_del_inlinekeyboard.delete()

                btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('shop_list_tooling')[0]), reply_markup=catalog_menu_btn_edit('shop_list_tooling'))#редактирую здесь была функция catalog_menu()
                global btn_counter 
                btn_counter = 0
                global inline_callback_cheker
                inline_callback_cheker = 'button_edit_tooling'
            
                
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")



# @dp.callback_query_handler(lambda c: c.data == 'table_edit')
async def edit_btn_tabl(callback_query: types.CallbackQuery):
    global db_name_btn
    db_name_btn = 'shop_list_table'
    global btn_del_inlinekeyboard
    if len(chek_db_telegram('shop_list_table')[1])>0:
                
                
                await btn_del_inlinekeyboard.delete()
                btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('shop_list_table')[0]), reply_markup=catalog_menu_btn_edit('shop_list_table'))#редактирую здесь была функция catalog_menu()
                global btn_counter 
                btn_counter = 0
                global inline_callback_cheker
                inline_callback_cheker = 'button_edit_table'
            
                
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")






# @dp.callback_query_handler(lambda c: c.data == 'other_products_edit')
async def edit_btn_other_products(callback_query: types.CallbackQuery):
    global db_name_btn


    db_name_btn = 'other_products_list'
    global btn_del_inlinekeyboard
    if len(chek_db_telegram('other_products_list')[1])>0:
                
                
                await btn_del_inlinekeyboard.delete()
                btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: " + str(chek_db_telegram('other_products_list')[0]), reply_markup=catalog_menu_btn_edit('other_products_list'))#редактирую здесь была функция catalog_menu()
                global btn_counter 
                btn_counter = 0
                global inline_callback_cheker
                inline_callback_cheker = 'button_edit_other'
            
                
    else:
        await bot.send_message(admin_id,"У вас нет активных товаров")


# @dp.callback_query_handler()
async def fsm_edit(callback_query: types.CallbackQuery):
     
     

    global fsm_price

    fsm_price = callback_query.data[5:]
    

    id_product = callback_query.message.text
    get_first_index = str(id_product).find(":")
    check = id_product[get_first_index+2:]
    get_last_index = str(check).find(" ")

    
    global state_id_db
    state_id_db = check[:get_last_index]
    global btn_del_inlinekeyboard
    await btn_del_inlinekeyboard.delete()
    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Введите новую инфорцию ")
    await edit_db.edit_info.set()


# @dp.message_handler(state=edit_db.edit_info)
async def take_tovar_info_and_start_questions(msg: types.Message, state: FSMContext):
    cheack_isdigit = str(msg.text).isdigit()
    
    global db_name_btn
    global state_id_db
    global fsm_price
    global btn_del_inlinekeyboard

    

    if 'price' in fsm_price:

        if cheack_isdigit == True:
            async with state.proxy() as data:
                data['edit_info'] = msg.text
            await edit_db.edit_info.set()
            
            await btn_del_inlinekeyboard.delete()


            edit_product_all(state_id_db,data['edit_info'],db_name_btn,fsm_price)
            await state.finish()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,"Товар изменен ", reply_markup=menu_frep())
        else:
            
            await btn_del_inlinekeyboard.delete()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,"Введите число!!!")
    
    else:

        async with state.proxy() as data:
            data['edit_info'] = msg.text
        await edit_db.edit_info.set()
        
        await btn_del_inlinekeyboard.delete()


        edit_product_all(state_id_db,data['edit_info'],db_name_btn,fsm_price)
        await state.finish()
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Товар изменен ", reply_markup=menu_frep())
        
        




# @dp.callback_query_handler(lambda c: c.data == 'product_edit_')
async def callback_check(callback_query: types.CallbackQuery):

    x = callback_query.data 
    zxc = callback_query.data
    
    global db_name_btn
    global btn_del_inlinekeyboard
   
    match db_name_btn:
         
        case 'shop_list_tooling':
            check_id = ''
            for i in x[13:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('shop_list_tooling',check_id)

            await btn_del_inlinekeyboard.delete()
             
            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы редактируете: '+str(check_id) +' ' + pd_name,reply_markup=inline_menu_red_tooling_return(db_name_btn,id_generator_del(x[13:])))

        case 'shop_list_table':
            check_id = ''
            for i in x[13:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('shop_list_table',check_id)
      
            await btn_del_inlinekeyboard.delete()
            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы редактируете: '+str(check_id) +' ' + pd_name,reply_markup=inline_menu_red_table_return(db_name_btn,id_generator_del(x[13:])))

        case 'other_products_list':
            check_id = ''
            for i in x[13:]:
                
                check_id += str(i)
                if i == ' ':
                    break    
            pd_name = check_db_product_name('other_products_list',check_id)

           
            
            await btn_del_inlinekeyboard.delete()

            btn_del_inlinekeyboard = await bot.send_message(admin_id,'вы редактируете: '+str(check_id) +' ' + pd_name,reply_markup=inline_menu_red_other)



#////////////////////////////////////////////////////////////////////////////////////////// Скрол страниц начало удаления

btn_counter = 0

# @dp.callback_query_handler(lambda c: c.data == 'btn_next_edit')
async def btn_next_edit(callback_query: types.CallbackQuery):
    global db_name_btn

    count_upper = 1
    global btn_counter
  
    btn_counter = catalog_menu_all_btn_edit(btn_counter,db_name_btn)[1] + count_upper

    global btn_del_inlinekeyboard
    await btn_del_inlinekeyboard.delete()
    

    
    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_edit(btn_counter,db_name_btn)[0])

# @dp.callback_query_handler(lambda c: c.data == 'btn_back_edit')
async def btn_back_edit(callback_query: types.CallbackQuery):
    count_upper = 1
    global btn_counter
    global btn_del_inlinekeyboard
    await btn_del_inlinekeyboard.delete()
    btn_counter = catalog_menu_all_btn_edit(btn_counter,db_name_btn)[1] - count_upper
    if btn_counter < 0:
        btn_counter = 0
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_edit(btn_counter,db_name_btn)[0])
    else:
        btn_del_inlinekeyboard = await bot.send_message(admin_id,"Все активные товары: "+str(chek_db_telegram(db_name_btn)[0]),reply_markup=catalog_menu_all_btn_edit(btn_counter,db_name_btn)[0])



#////////////////////////////////////////////////////////////////////////////////////////// Скрол страниц конец удаления












def reg_handler_edit(dp: Dispatcher):

    




    dp.register_message_handler(edit_product,text='Редактировать объявления')

    dp.register_callback_query_handler(edit_btn_tooling, lambda c: c.data == 'tooling_edit')

    dp.register_callback_query_handler(edit_btn_tabl, lambda c: c.data == 'table_edit')

    dp.register_callback_query_handler(edit_btn_other_products, lambda c: c.data == 'other_products_edit')





    #edit db
    dp.register_callback_query_handler(fsm_edit, text_startswith='edit_')

    dp.register_message_handler(take_tovar_info_and_start_questions, state=edit_db.edit_info)





    #Скрол страниц
    dp.register_callback_query_handler(btn_next_edit, lambda c: c.data == 'btn_next_edit')

    dp.register_callback_query_handler(btn_back_edit, lambda c: c.data == 'btn_back_edit')


    #Callback check
    dp.register_callback_query_handler(callback_check, text_startswith='product_edit_')

