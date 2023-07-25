from aiogram import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from math import ceil
from aiogram.utils.callback_data import CallbackData
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlite3 import Error
import os
import sys
from math import ceil
sys.path.insert(1,os.path.abspath('../laserbit/'))
from DB.db import *



# меню удаления товаров 
inline_btn_1 = InlineKeyboardButton('Выбрать товар', callback_data='button_del_focus')
inline_btn_2 = InlineKeyboardButton('Удалить весь каталог', callback_data='button_del_full_db')
inline_menu_delete_product = InlineKeyboardMarkup().add(inline_btn_1,inline_btn_2)


# меню редактирования tooling 
def inline_menu_red_tooling_return(db_name, db_id):
    inline_btn_tooling_name_towar= InlineKeyboardButton('Изменить имя товара', callback_data='edit_name_product')
    inline_btn_tooling_price = InlineKeyboardButton('Изменить цену товара: '+str(check_db_price(db_name,db_id,'product_price'))+'р', callback_data='edit_product_price')
    inline_btn_tooling_full_description = InlineKeyboardButton('Изменить полное описание товара', callback_data='edit_full_description')
    inline_btn_tooling_metal_thickness = InlineKeyboardButton('Изменить толщину металла товара', callback_data='edit_metal_thickness')
    inline_menu_red_tooling = InlineKeyboardMarkup(row_width=1).add(inline_btn_tooling_name_towar,inline_btn_tooling_price,inline_btn_tooling_full_description,inline_btn_tooling_metal_thickness)
    return inline_menu_red_tooling




# меню редактирования table
def inline_menu_red_table_return(db_name, db_id):

    

    inline_btn_table_name_towar= InlineKeyboardButton('Изменить имя товара', callback_data='edit_name_product')
    inline_btn_table_price_4 = InlineKeyboardButton('Изменить цену товара для 4мм: '+str(check_db_price(db_name,db_id,'price_4'))+'р', callback_data='edit_price_4')
    inline_btn_table_price_5 = InlineKeyboardButton('Изменить цену товара для 5мм: '+str(check_db_price(db_name,db_id,'price_5'))+'р', callback_data='edit_price_5')
    inline_btn_table_price_6 = InlineKeyboardButton('Изменить цену товара для 6мм: '+str(check_db_price(db_name,db_id,'price_6'))+'р', callback_data='edit_price_6')
    inline_btn_table_price_8 = InlineKeyboardButton('Изменить цену товара для 8мм: '+str(check_db_price(db_name,db_id,'price_8'))+'р', callback_data='edit_price_8')
    inline_btn_table_price_10 = InlineKeyboardButton('Изменить цену товара для 10мм: '+str(check_db_price(db_name,db_id,'price_10'))+'р', callback_data='edit_price_10')
    inline_btn_table_price_12 = InlineKeyboardButton('Изменить цену товара для 12мм: '+str(check_db_price(db_name,db_id,'price_12'))+'р', callback_data='edit_price_12')
    assembly_price = InlineKeyboardButton('Изменить цену товара для сборки: '+str(check_db_price(db_name,db_id,'assembly_price'))+'р', callback_data='edit_assembly_price')
    inline_btn_table_full_description = InlineKeyboardButton('Изменить полное описание товара', callback_data='edit_full_description')
    inline_btn_table_size = InlineKeyboardButton('Изменить полное размер стола', callback_data='edit_Size_Table')
    inline_btn_table_material = InlineKeyboardButton('Изменить материал стола', callback_data='edit_Material_Table')

    inline_menu_red_table = InlineKeyboardMarkup(row_width=1).add(inline_btn_table_name_towar,inline_btn_table_full_description,
                                                                inline_btn_table_size,inline_btn_table_material,inline_btn_table_price_4,
                                                                inline_btn_table_price_5,inline_btn_table_price_6,inline_btn_table_price_8,inline_btn_table_price_10,inline_btn_table_price_12,assembly_price)
    return(inline_menu_red_table)








# меню редактирования other
inline_btn_other_name_towar= InlineKeyboardButton('Изменить имя товара', callback_data='edit_name_product')
inline_btn_other_full_description = InlineKeyboardButton('Изменить полное описание товара', callback_data='edit_full_description')
inline_menu_red_other = InlineKeyboardMarkup(row_width=1).add(inline_btn_other_name_towar,inline_btn_other_full_description)






confirmation_yes = InlineKeyboardButton('Да', callback_data='confirmation_yes') 
confirmation_no = InlineKeyboardButton('Нет', callback_data='confirmation_no')
goods_confirmation = InlineKeyboardMarkup().add(confirmation_yes,confirmation_no)
   

     
# меню выбора товара при создании
product_tooling = InlineKeyboardButton('Оснастка', callback_data='shop_list_tooling') 
product_table = InlineKeyboardButton('Стол', callback_data='shop_list_table')
product_other = InlineKeyboardButton('Прочее', callback_data='other_products_list')
product_btn_group = InlineKeyboardMarkup().add(product_tooling,product_table,product_other)



# меню выбора товара при удалении товара
product_tooling_del = InlineKeyboardButton('Оснастка', callback_data='tooling_del') 
product_table_del = InlineKeyboardButton('Стол', callback_data='table_del')
product_other_del = InlineKeyboardButton('Прочее', callback_data='other_products_del')
product_btn_group_del_call = InlineKeyboardMarkup().add(product_tooling_del,product_table_del,product_other_del)


# меню выбора товара при редактировании товара
product_tooling_edit = InlineKeyboardButton('Оснастка', callback_data='tooling_edit') 
product_table_edit = InlineKeyboardButton('Стол', callback_data='table_edit')
product_other_edit = InlineKeyboardButton('Прочее', callback_data='other_products_edit')
product_btn_group_edit_call = InlineKeyboardMarkup().add(product_tooling_edit,product_table_edit,product_other_edit)





#/////////////////////////////////////////////////////////////////////////create inline button 

def create_inline_btn(name_db, call_back):
    len_items, items = chek_db_telegram(name_db)
    inline_catalog_menu_keyboard_array = InlineKeyboardMarkup()

    for i in range(len_items): 
        items_counter = items[i]
        button_label = str(items_counter[0]) + ' ' + str(items_counter[1])
     
        button_label = button_label[:64]
        inline_catalog_menu_keyboard_array.add(
            InlineKeyboardButton(button_label, callback_data=call_back + str(items_counter[0]) + ' ' + str(name_db))
        )

    len_inline_catalog_menu_array = len(inline_catalog_menu_keyboard_array.inline_keyboard)
    arrat_inline_keyboard = inline_catalog_menu_keyboard_array.inline_keyboard
    full_aray_number_of_pages = []
    number_of_pages = ceil(len_inline_catalog_menu_array / 5) 

    for j in range(number_of_pages):
        full_aray_number_of_pages.append(arrat_inline_keyboard[0:5])
        del arrat_inline_keyboard[0:5]
            
    return full_aray_number_of_pages




def catalog_menu_btn_edit(name_db):

    btn_next = InlineKeyboardButton('➡️', callback_data='btn_next_edit')
    btn_back = InlineKeyboardButton('⬅️', callback_data='btn_back_edit')
    result = {'inline_keyboard': create_inline_btn(name_db,'product_edit_')[0]}
    
    result['inline_keyboard'].append([btn_back,btn_next])
 
    return result

 


def catalog_menu_all_btn_edit(counter,name_db):
    btn_next = InlineKeyboardButton('➡️', callback_data='btn_next_edit')
    btn_back = InlineKeyboardButton('⬅️', callback_data='btn_back_edit')
    if counter < len(create_inline_btn(name_db,'product_edit_')) or counter != len(create_inline_btn(name_db,'product_edit_')):
        result = {'inline_keyboard': create_inline_btn(name_db,'product_edit_')[counter]}
        result['inline_keyboard'].append([btn_back,btn_next])
    
        return result, counter
    else:
        counter = 0
        result = {'inline_keyboard': create_inline_btn(name_db,'product_edit_')[counter]}
        result['inline_keyboard'].append([btn_back,btn_next])
    
        return result, counter








def catalog_menu_btn_del(name_db):

    btn_next = InlineKeyboardButton('➡️', callback_data='btn_next_del')
    btn_back = InlineKeyboardButton('⬅️', callback_data='btn_back_del')
    result = {'inline_keyboard': create_inline_btn(name_db,'product_delete_')[0]}

  
    
    result['inline_keyboard'].append([btn_back,btn_next])
    
    return result

 


def catalog_menu_all_btn_del(counter,name_db):
    btn_next = InlineKeyboardButton('➡️', callback_data='btn_next_del')
    btn_back = InlineKeyboardButton('⬅️', callback_data='btn_back_del')
    
    if counter < len(create_inline_btn(name_db,'product_delete_')) or counter != len(create_inline_btn(name_db,'product_delete_')):
        result = {'inline_keyboard': create_inline_btn(name_db,'product_delete_')[counter]}
        result['inline_keyboard'].append([btn_back,btn_next])
    
        return result, counter
    else:
        counter = 0
        result = {'inline_keyboard': create_inline_btn(name_db,'product_delete_')[counter]}
        result['inline_keyboard'].append([btn_back,btn_next])
    
        return result, counter


