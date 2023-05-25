from aiogram import *
from config import *
from KeyboardMarkup.ReplyKeyboardMarkup import *
from inlinekey.InlineKeyBoard import *
import sqlite3
from sqlite3 import Error
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from Main_function.Edit_Folder import *
import os
import sys
from aiogram.types import CallbackQuery, Message
from Main_function.State_group import *
sys.path.insert(1,os.path.abspath('../Marketplace/'))
from DB.db import init_db,add_message_shop_list_table,add_message_shop_list_tooling,read_sqlite_table
from aiogram.dispatcher.filters import Text
bot = Bot(token)









# @dp.message_handler(state="*", commands='Отмена')
# @dp.message_handler(Text(equals='Отмена',ignore_case=True),state="*")
async def breack(message: types.Message, state: FSMContext):
        
        
        global db_name
        global name_root_folder
        global folder_name_id
        global btn_del_inlinekeyboard 

        

        if folder_name_id in os.listdir(f'''static/img/img_shop/{name_root_folder}/''') and folder_name_id != False:

            
            focus_del_item_pos(folder_name_id,db_name)
            focus_del_img_folder(folder_name_id,db_name)
            await state.finish()
            
            btn_del_inlinekeyboard = await message.answer("Операция отменена",reply_markup=menu_frep())
        else:
            await state.finish()
            btn_del_inlinekeyboard = await message.answer("Операция отменена",reply_markup=menu_frep())
    






# @dp.message_handler(text='Добавить объявления')
async def add_KeyboardMarkup(message: types.Message):
    global folder_name_id
    folder_name_id = False

    numb_colums_tooling = read_sqlite_table('id','shop_list_tooling')
    numb_colums_table = read_sqlite_table('id','shop_list_table')
    numb_colums_other = read_sqlite_table('id','other_products_list')
    summ_db = int(numb_colums_tooling) + int(numb_colums_table) + int(numb_colums_other)


    msg = str(message.from_id)
    if admin_id == msg:
        if int(summ_db) > 0:
            global btn_del_inlinekeyboard

        
            btn_del_inlinekeyboard = await message.reply(f'''Активных {str(summ_db)} объявлений

оснастка = {numb_colums_tooling}
столов = {numb_colums_table}
прочее = {numb_colums_other}

Выберите какой товар вы хотите добавить''', reply_markup=product_btn_group)
            
        else:
            btn_del_inlinekeyboard = await bot.send_message(admin_id,"У вас 0 объяв, Выберите какой товар вы хотите добавить", reply_markup=product_btn_group)
        
    else:
        await bot.send_message(msg,"Вы не админ,у вас нет прав доступа!")







#////////////////////////////////////////////////////////////////////////////////////////////////Filter при выборе товара начало


# @dp.callback_query_handler(lambda c: c.data == 'shop_list_tooling')
async def process_callback__tooling(callback_query: types.CallbackQuery):
    
    global db_name
    global name_root_folder
    
    db_name = callback_query.data
    name_root_folder = 'tooling'
    

    global btn_del_inlinekeyboard


    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Введите название для товара",reply_markup=keyboard_cancellation)

    await Db_tooling.name_towar.set() 




# @dp.callback_query_handler_table(lambda c: c.data == 'shop_list_table')
async def process_callback__table(callback_query: types.CallbackQuery):

    global db_name
    global name_root_folder
    
    db_name = callback_query.data
    name_root_folder = 'table'
    

    global btn_del_inlinekeyboard


    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Введите название для товара",reply_markup=keyboard_cancellation)

    await Db_table.name_towar.set() 




# @dp.callback_query_handler_products(lambda c: c.data == 'other_products_list')
async def process_callback_products(callback_query: types.CallbackQuery):

    global db_name
    global name_root_folder

    db_name = callback_query.data
    name_root_folder = 'other_product'
    

    global btn_del_inlinekeyboard


    btn_del_inlinekeyboard = await bot.send_message(admin_id,"Введите название для товара",reply_markup=keyboard_cancellation)

    await Db_other_product.name_towar.set() 





#////////////////////////////////////////////////////////////////////////////////////////////////Filter при выборе товара конец








#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА ПРОЧЕЕ В БД НАЧАЛО

# @dp.message_handler(state=Db_other_product.name_towar)
async def take_tovar_name_and_start_questions_other_product(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name_towar'] = msg.text
    global name_towar
    name_towar = str(data['name_towar'])
    name_towar = name_towar.replace(' ','_')
    await bot.send_message(admin_id,"Введите цену для "+name_towar, reply_markup=keyboard_cancellation)
    await Db_other_product.price.set()




# @dp.message_handler(state=Db_tooling.price)
async def take_tovar_price_other_product(msg: types.Message,state: FSMContext):
   global price
   async with state.proxy() as data:
        if msg.text.isdigit():
            data['price'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
        
        price = data['price']
        await bot.send_message(admin_id, f"Введи краткое описание", reply_markup=keyboard_cancellation)
        await Db_other_product.description.set()
        




    


# @dp.message_handler(state=Db_other_product.description)
async def take_tovar_description_other_product(msg: types.Message,state: FSMContext):
      
    async with state.proxy() as data:
        data['description'] = msg.text
    check_db('other_products_list')
    global product_id
    global name_towar
    global folder_name_cancellation
    global folder_name_id
    product_id = get_last_id('other_products_list')
    folder_name_id = str(product_id)
    folder_name_cancellation = str(product_id)+'_'+str(name_towar)

    creat_img_folder(str(folder_name_cancellation),'other_product')


    add_message_shop_list_other(name_product=str(data['name_towar']), price=int(data['price']), full_description=str(data['description']),name_db = 'other_products_list') #ЗАПИСЬ В БД
    check_db('other_products_list')
    await bot.send_message(admin_id,'Добавьте фото товара', reply_markup=keyboard_cancellation) 
    await Db_other_product.product_preview.set()





#///////////////////////////////////////////////////////////////////////////////////////////  Скачивание и проверка фото 


# @dp.message_handler(state=Db_other_product.product_preview, content_types=types.ContentTypes.ANY) 
async def get_migrabank_other_product(message: types.Message, state: FSMContext):

    if message.photo:
        fileID = message.photo[-1].file_id
        await state.update_data(fobackbankcard=f"{fileID}")
        await message.photo[-1].download('static/img/img_shop/other_product/'+str(product_id)+'/'+str(product_id)+'.jpg')
        await message.photo[-1].download('static/img/img_shop/other_product/'+str(product_id)+'/'+'img'+'/'+str(product_id)+'.jpg')
        await bot.send_message(admin_id,"Отпрвьте группу фото", reply_markup=keyboard_btn_photo())
        await Db_other_product.product_group.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_cancellation)






# @dp.message_handler(state=Db_other_product.product_group, content_types=types.ContentTypes.ANY) 
async def get_migrabank_group_other_product(message: types.Message, state: FSMContext):
    
    if message.photo:
        photoSize = message.photo[-1]
        file_info = await bot.get_file(photoSize.file_id)
        fileExt = file_info.file_path.split(".")[-1]
        await message.photo[-1].download('static/img/img_shop/other_product/'+str(product_id)+'/'+'img'+'/'+f"{photoSize.file_unique_id}.{fileExt}")
        
    elif message.text == 'Создать объявление':
        await state.finish()
        await bot.send_message(chat_id=message.chat.id, text=f'''Товар создан''', reply_markup=menu_frep())

    else:
        
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_btn_photo())




#///////////////////////////////////////////////////////////////////////////////////////////Скачивание и проверка фото 


#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА ПРОЧЕЕ В БД КОНЕЦ













#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА ОСНАСТКА В БД НАЧАЛО
# @dp.message_handler(state=Db_tooling.name_towar)
async def take_tovar_name_and_start_questions_tooling (msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name_towar'] = msg.text
    global name_towar
    name_towar = str(data['name_towar'])
    name_towar = name_towar.replace(' ','_')
    await bot.send_message(admin_id,"Введите цену "+name_towar, reply_markup=keyboard_cancellation)
    await Db_tooling.price.set()

    
# @dp.message_handler(state=Db_tooling.price)
async def take_tovar_price_tooling(msg: types.Message,state: FSMContext):
    global price
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
        
        price = data['price']
        await bot.send_message(admin_id, f"Введи краткое описание", reply_markup=keyboard_cancellation)
        await Db_tooling.full_description.set()




# @dp.message_handler(state=Db_tooling.full_description)
async def take_tovar_full_description_tooling(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['full_description'] = msg.text
    
    check_db('shop_list_tooling')
    
    global product_id
    global name_towar
    global folder_name_cancellation
    global folder_name_id
    product_id = get_last_id('shop_list_tooling')
    folder_name_id = str(product_id)
    folder_name_cancellation = str(product_id)+'_'+str(name_towar)
    creat_img_folder(str(folder_name_cancellation),'tooling')
    add_message_shop_list_tooling(name_product=str(data['name_towar']), product_price=str(data['price']), full_description=str(data['full_description']),name_db = 'shop_list_tooling') #ЗАПИСЬ В БД
    check_db('shop_list_tooling')
    await bot.send_message(admin_id,'Добавьте фото товара', reply_markup=keyboard_cancellation) 
    await Db_tooling.product_preview.set()


#///////////////////////////////////////////////////////////////////////////////////////////  Скачивание и проверка фото 
# @dp.message_handler(state=Db_tooling.product_preview, content_types=types.ContentTypes.ANY) 
async def get_migrabank_tooling(message: types.Message, state: FSMContext):

    if message.photo:
        fileID = message.photo[-1].file_id
        await state.update_data(fobackbankcard=f"{fileID}")
        await message.photo[-1].download('static/img/img_shop/tooling/'+str(product_id)+'/'+str(product_id)+'.jpg')
        await message.photo[-1].download('static/img/img_shop/tooling/'+str(product_id)+'/'+'img'+'/'+str(product_id)+'.jpg')
        await bot.send_message(admin_id,"Отпрвьте группу фото", reply_markup=keyboard_btn_photo())
        await Db_tooling.product_group.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_cancellation)






# @dp.message_handler(state=Db_tooling.product_group, content_types=types.ContentTypes.ANY) 
async def get_migrabank_group_tooling(message: types.Message, state: FSMContext):
    
    if message.photo:
        photoSize = message.photo[-1]
        file_info = await bot.get_file(photoSize.file_id)
        fileExt = file_info.file_path.split(".")[-1]
        await message.photo[-1].download('static/img/img_shop/tooling/'+str(product_id)+'/'+'img'+'/'+f"{photoSize.file_unique_id}.{fileExt}")
        

    elif message.text == 'Создать объявление':
        await state.finish()
        await bot.send_message(chat_id=message.chat.id, text=f'''Товар создан''', reply_markup=menu_frep())

    else:
        
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_btn_photo())

#///////////////////////////////////////////////////////////////////////////////////////////Скачивание и проверка фото 




#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА ОСНАСТКА В БД КОНЕЦ

















#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА СТОЛ В БД НАЧАЛО

# @dp.message_handler(state=Db_table.name_towar)
async def take_tovar_name_table(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name_towar'] = msg.text
    global name_towar
    name_towar = str(data['name_towar'])
    name_towar = name_towar.replace(' ','_')
    await bot.send_message(admin_id,"Введите цену на 4мм для товара "+name_towar, reply_markup=keyboard_cancellation)
    await Db_table.price_4.set()

    
    

#//////////////////////////////////////////////////////////////////////////////////////////////////////PRICE START

# @dp.message_handler(state=Db_table.price)
async def take_tovar_price_table_4(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_4'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_4']
    await bot.send_message(admin_id, f"Введите цену на 5мм для товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.price_5.set()



# @dp.message_handler(state=Db_table.price)
async def take_tovar_price_table_5(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_5'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_5']
    await bot.send_message(admin_id, f"Введите цену на 6мм для товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.price_6.set()
       


# @dp.message_handler(state=Db_table.price)
async def take_tovar_price_table_6(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_6'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_6']
    await bot.send_message(admin_id, f"Введите цену на 8мм для товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.price_8.set()



# @dp.message_handler(state=Db_table.price)
async def take_tovar_price_table_8(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_8'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_8']
    await bot.send_message(admin_id, f"Введите цену на 10мм для товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.price_10.set()



async def take_tovar_price_table_10(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_10'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_10']
    await bot.send_message(admin_id, f"Введите цену на 12мм для товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.price_12.set()





# @dp.message_handler(state=Db_table.price)
async def take_tovar_price_table_12(msg: types.Message,state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['price_12'] = int(msg.text)
        else:
            await bot.send_message(admin_id, "Введите число", reply_markup=keyboard_cancellation)
            return
    global price
    price = data['price_12']
    await bot.send_message(admin_id, f"Введите описание товара {name_towar}", reply_markup=keyboard_cancellation)
    await Db_table.full_description.set()  
    
#//////////////////////////////////////////////////////////////////////////////////////////////////////////PRICE END





# @dp.message_handler(state=Db_table.full_description)
async def take_tovar_full_description_table(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['full_description'] = msg.text
    
        await bot.send_message(admin_id,"Введи размер стола "+name_towar, reply_markup=keyboard_cancellation)
        await Db_table.Size_Table.set()




# @dp.message_handler(state=Db_table.Size_Table)
async def take_tovar_size(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['Size_Table'] = msg.text
        
    
        await bot.send_message(admin_id,"Введи материал стола "+name_towar, reply_markup=keyboard_cancellation)
        await Db_table.Material_Table.set()







# @dp.message_handler(state=Db_table.Material_Table)
async def take_tovar_material_table(msg: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['Material_Table'] = msg.text
    
    check_db('shop_list_table')
    global product_id
    global name_towar
    global folder_name_cancellation
    global folder_name_id
    product_id = get_last_id('shop_list_table')
    folder_name_id = str(product_id)
    folder_name_cancellation = str(product_id)+'_'+str(name_towar)
    creat_img_folder(str(folder_name_cancellation),'table')
    add_message_shop_list_table(name_product=str(data['name_towar']), price_4=int(data['price_4']), price_5=int(data['price_5']), price_6=int(data['price_6']), price_8=int(data['price_8']), price_10=int(data['price_10']), price_12=int(data['price_12']), full_description=str(data['full_description']), Size_Table=str(data['Size_Table']), Material_Table=str(data['Material_Table']),name_db = 'shop_list_table') #ЗАПИСЬ В БД
    check_db('shop_list_table')
    await bot.send_message(admin_id,'Добавьте фото для карточки товара', reply_markup=keyboard_cancellation) 
    await Db_table.product_preview.set()




#///////////////////////////////////////////////////////////////////////////////////////////  Скачивание и проверка фото 
# @dp.message_handler(state=Db_table.product_preview, content_types=types.ContentTypes.ANY) 
async def get_migrabank_table(message: types.Message, state: FSMContext):

    if message.photo:
        fileID = message.photo[-1].file_id
        await state.update_data(fobackbankcard=f"{fileID}")
        await message.photo[-1].download('static/img/img_shop/table/'+str(product_id)+'/'+str(product_id)+'.jpg')
        await message.photo[-1].download('static/img/img_shop/table/'+str(product_id)+'/'+'img'+'/'+str(product_id)+'.jpg')
        await bot.send_message(admin_id,"Отпрвьте группу фото", reply_markup=keyboard_btn_photo())
        await Db_table.product_group.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_cancellation)






# @dp.message_handler(state=Db_table.product_group, content_types=types.ContentTypes.ANY) 
async def get_migrabank_group_table(message: types.Message, state: FSMContext):
    
    if message.photo:
        photoSize = message.photo[-1]
        file_info = await bot.get_file(photoSize.file_id)
        fileExt = file_info.file_path.split(".")[-1]
        await message.photo[-1].download('static/img/img_shop/table/'+str(product_id)+'/'+'img'+'/'+f"{photoSize.file_unique_id}.{fileExt}")

    elif message.text == 'Создать объявление':
        await state.finish()
        await bot.send_message(chat_id=message.chat.id, text=f'''Товар создан''', reply_markup=menu_frep())

    else:
        
        await bot.send_message(chat_id=message.chat.id, text=f'''Вы отправили что-то не то. Отправьте фото!''', reply_markup=keyboard_btn_photo())

#///////////////////////////////////////////////////////////////////////////////////////////Скачивание и проверка фото 



#////////////////////////////////////////////////////////////////////////////////////////// ЗАПИСЬ ТОВАРА СТОЛ В БД КОНЕЦ




















def reg_handler_add(dp: Dispatcher):

    dp.register_message_handler(breack,Text(equals='Отмена',ignore_case=True),state="*")

    
    dp.register_message_handler(add_KeyboardMarkup,text='Добавить объявления')
    


    #callback check other
    dp.register_callback_query_handler(process_callback_products,lambda c: c.data =='other_products_list')

    dp.register_message_handler(take_tovar_name_and_start_questions_other_product,state=Db_other_product.name_towar)

    dp.register_message_handler(take_tovar_price_other_product,state=Db_other_product.price)

    dp.register_message_handler(take_tovar_description_other_product,state=Db_other_product.description)

    dp.register_message_handler(get_migrabank_other_product,state=Db_other_product.product_preview, content_types=types.ContentTypes.ANY)

    dp.register_message_handler(get_migrabank_group_other_product,state=Db_other_product.product_group, content_types=types.ContentTypes.ANY)



    #callback check tooling
    dp.register_callback_query_handler(process_callback__tooling,lambda c: c.data =='shop_list_tooling')

    dp.register_message_handler(take_tovar_name_and_start_questions_tooling,state=Db_tooling.name_towar)

    dp.register_message_handler(take_tovar_price_tooling, state=Db_tooling.price)



    dp.register_message_handler(take_tovar_full_description_tooling,state=Db_tooling.full_description)

    dp.register_message_handler(get_migrabank_tooling,state=Db_tooling.product_preview, content_types=types.ContentTypes.ANY)

    dp.register_message_handler(get_migrabank_group_tooling,state=Db_tooling.product_group, content_types=types.ContentTypes.ANY)



    #callback check table
    dp.register_callback_query_handler(process_callback__table,lambda c: c.data =='shop_list_table')

    dp.register_message_handler(take_tovar_name_table,state=Db_table.name_towar)



    dp.register_message_handler(take_tovar_price_table_4,state=Db_table.price_4)

    dp.register_message_handler(take_tovar_price_table_5,state=Db_table.price_5)

    dp.register_message_handler(take_tovar_price_table_6,state=Db_table.price_6)

    dp.register_message_handler(take_tovar_price_table_8,state=Db_table.price_8)

    dp.register_message_handler(take_tovar_price_table_10,state=Db_table.price_10)
    dp.register_message_handler(take_tovar_price_table_12,state=Db_table.price_12)




    dp.register_message_handler(take_tovar_full_description_table, state=Db_table.full_description)

    dp.register_message_handler(take_tovar_size, state=Db_table.Size_Table)

    dp.register_message_handler(take_tovar_material_table, state=Db_table.Material_Table)

    dp.register_message_handler(get_migrabank_table,state=Db_table.product_preview, content_types=types.ContentTypes.ANY)

    dp.register_message_handler(get_migrabank_group_table, state=Db_table.product_group, content_types=types.ContentTypes.ANY)





