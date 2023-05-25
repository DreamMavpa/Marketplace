from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from sqlite3 import Error
from datetime import datetime
from flask import jsonify
import os
import subprocess
from waitress import serve
from TgBot.config import token,admin_id
app = Flask(__name__)
import requests
import json



def  create_connection_db():
    
    global connection
    connection = sqlite3.connect('DB/Database.db')
    return connection

# Передача jsona c img на фронт 

def drop_json_front():

    db_arr = ['shop_list_tooling','shop_list_table','other_products_list']

    
    full_dict = {
        'shop_list_tooling':'-',
        'shop_list_table':'-',
        'other_products_list':'-'
    }
   
    for j in db_arr:
        img_list = []
        conn = create_connection_db()
        c = conn.cursor()
        record = c.execute(f'''SELECT id FROM {j}''')
        check_db =  c.fetchall()


        
        for i in check_db:
           
                img_list.append(str(i[0]))

        full_dict[j] = img_list

    
    return full_dict

def get_img(db_img):

    name_img_dict = {}
    full_data_dict = {}

    db_arr = ['shop_list_table','shop_list_tooling','other_products_list']
    name_folder_arr = ['table','tooling','other_product']
 
    for k in range(3):

        for i in db_img[db_arr[k]]:
            test = os.walk(f'''static\\img\\img_shop\\{name_folder_arr[k]}\\{i}\\img''')
        
            path, dirs, files = next(test)
            
            for j in files:
                connection_id_name = str(i[0:])
                name_img_dict[connection_id_name] = name_img_dict.get(connection_id_name, []) + [j]

        full_data_dict[db_arr[k]] = name_img_dict
        name_img_dict = {}
    return full_data_dict


@app.route('/api')
def api():
    return jsonify(get_img(drop_json_front()))

@app.route("/")
def index():
    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM shop_list_tooling')
    items_tooling =  c.fetchall()
    items_tooling.append('items_tooling')

    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM shop_list_table')
    items_table =  c.fetchall()
    items_table.append('items_table')

    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM other_products_list')
    other_products =  c.fetchall()
    other_products.append('other_products')

    json_index = get_img(drop_json_front())
    return render_template("index.html", items_tooling=items_tooling ,items_table=items_table, other_products=other_products, json_index=json_index)

#//////////////////////////////////////////////////////////////////////////////////

@app.route("/tables")
def tables():
    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM shop_list_table')
    items_table =  c.fetchall()

    return render_template("tables.html", items_table=items_table)

@app.route("/tooling")
def tooling():
    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM shop_list_tooling')
    items_tooling =  c.fetchall()

    return render_template("tooling.html", items_tooling=items_tooling)

@app.route("/others")
def other_products():
    conn = create_connection_db()
    c = conn.cursor()
    record = c.execute('SELECT * FROM other_products_list')
    other_products =  c.fetchall()

    return render_template("others.html", other_products=other_products)


@app.route('/<tb>/product-modal/<id>')
def id(tb,id):
    
    if tb == 'table':
        conn = create_connection_db()
        c = conn.cursor()
        record = c.execute("SELECT * FROM shop_list_table WHERE id = ?", (id, ))
        list_json = c.fetchall()
        product_type = 'table'
        db_name = 'shop_list_table'

        list_mm = ['4mm','5mm','6mm','8mm','10mm','12mm']
     

        price_mm = {}

        first_item = []
        for i in range(2,8):
            if list_json[0][i] != 0:
                price_mm[list_mm[i-2]] = str(list_json[0][i])
                first_item.append(str(list_json[0][i]))



    elif tb == 'tooling':
        conn = create_connection_db()
        c = conn.cursor()
        record = c.execute("SELECT * FROM shop_list_tooling WHERE id = ?", (id, ))
        list_json = c.fetchall()
        product_type = 'tooling'
        db_name = 'shop_list_tooling'
        first_item = list_json[0][2]
        price_mm=None

    elif tb == 'others':
        conn = create_connection_db()
        c = conn.cursor()
        record = c.execute("SELECT * FROM other_products_list WHERE id = ?", (id, ))
        list_json = c.fetchall()
        product_type = 'products_list'
        db_name = 'other_products_list'
        tb = 'other_product'
        first_item = list_json[0][2]
        price_mm=None

    record = c.execute('SELECT * FROM shop_list_tooling')
    items_tooling =  c.fetchall()

    record = c.execute('SELECT * FROM shop_list_table')
    items_table =  c.fetchall()
    
    record = c.execute('SELECT * FROM other_products_list')
    items_other =  c.fetchall()

 
    return render_template("product-modal.html",  list_json=list_json,first_item=first_item, price_mm=price_mm, items_table=items_table,
                            items_tooling=items_tooling, items_other=items_other, tb=tb, db_name = db_name,product_type=product_type)







@app.route('/jsondrop', methods=['POST'])
def drop_in_tg():
    
    request_data = request.get_data()
    request_dict = json.loads(request_data.decode('utf-8'))

    items = ''
    all_price = 0
 
    print(request_dict)
    for i in range(len(request_dict)-1):

        # if request_dict[i]['type'] == 'other':
        #     items += 'Тип продукта: '+request_dict[i]['type']+' Название: '+request_dict[i]['name']+'\n'

        if len(request_dict[i]['name']) <= 13: 
            items += ' Тип продукта: '+str(request_dict[i]['type'])+'\n'+' Название: '+str(request_dict[i]['name'])+'\n'+' Цена: '+str(request_dict[i]['price'])+'\n''---------------------------------------------------------------'+'\n'
            all_price += int(request_dict[i]['price'])
        else:
            items += ' Тип продукта: '+str(request_dict[i]['type'])+'\n'+' Название: '+str(request_dict[i]['name'][:20])+'...'+'\n'+' Цена: '+str(request_dict[i]['price'])+'\n''---------------------------------------------------------------'+'\n'
            all_price += int(request_dict[i]['price'])
    
    
    form_info = f'''
Заказ LaserBit

Имя: {request_dict[-1]['name']}
Номер телефона: {request_dict[-1]['tel']}
Почта: {request_dict[-1]['email']}
Адрес: {request_dict[-1]['shippingAddress']}
Комментарий: {request_dict[-1]['comment']}
---------------------------------------------------------------
{items}
Общая цена заказа: {all_price}р
       '''
        
        
    requests.get(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={admin_id}&text={form_info}''')
    
    return redirect('/')







if __name__ == "__main__":

    serve(app, host="localhost", port=8080)