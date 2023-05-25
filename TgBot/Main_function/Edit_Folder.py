from aiogram import *
import os
import sys
import shutil





def creat_img_folder(name_folder,db_name):
        filter_index = str(name_folder).find('_')
        
        dir = f'''static/img/img_shop/{db_name}/{str(name_folder[:filter_index])}/'''
       
        os.mkdir(dir)


def drop_img():
        path = os.path.join(os.path.abspath(os.path.dirname(f'''static/img/''')), 'img_shop')
        shutil.rmtree(path)
        os.mkdir('static/img/img_shop')
        os.mkdir('static/img/img_shop/tooling')
        os.mkdir('static/img/img_shop/table')
        os.mkdir('static/img/img_shop/other_product')


def focus_del_img_folder(name_folder_id,name_bd):
        

        if name_bd == 'shop_list_tooling':
                path = os.path.join(os.path.abspath(os.path.dirname(f'''static/img/img_shop/tooling/{name_folder_id}''')), name_folder_id)
                shutil.rmtree(path)

        elif name_bd == 'shop_list_table':
                path = os.path.join(os.path.abspath(os.path.dirname(f'''static/img/img_shop/table/{name_folder_id}''')), name_folder_id)
                shutil.rmtree(path)

        elif name_bd == 'other_products_list':
                path = os.path.join(os.path.abspath(os.path.dirname(f'''static/img/img_shop/other_product/{name_folder_id}''')), name_folder_id)
                shutil.rmtree(path)
        else:
                print('НЕТ УСЛОВИЯ В ФУНКЦИИ focus_del_img_folder()')






def name_folder_generator_del(product_name):
        gener_name = ''
        for i in range(len(product_name)):
                if product_name[i].isdigit() == True:
                        gener_name += product_name[i]
                elif product_name[i] == ' ':
                        gener_name += product_name[i].replace(' ','_')
                else:
                        gener_name += product_name[i]
        return gener_name






def id_generator_del(product_id):
        gener_id = ''
        for i in range(len(product_id)):
                if product_id[i].isdigit() == True:
                        gener_id += str(product_id[i])
                else:
                        break
        return gener_id


