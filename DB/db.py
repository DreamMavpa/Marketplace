import sqlite3
from sqlite3 import Error


#db conector
connection = None



def create_connection():
    
    global connection
    if connection is None:
        connection = sqlite3.connect('DB/Database.db')

    return connection


def init_db(force:bool = False):
    conn = create_connection()
    c = conn.cursor()


    if force:
        c.execute('DROP TABLE IF EXISTS shop_list_tooling')
        c.execute('DROP TABLE IF EXISTS shop_list_table')
        c.execute('DROP TABLE IF EXISTS other_products_list')
    

    c.execute('''CREATE TABLE IF NOT EXISTS shop_list_table (
        id INTEGER,
        name_product TEXT,
        price_4 INT,
        price_5 INT,
        price_6 INT,
        price_8 INT,
        price_10 INT,
        price_12 INT,
        assembly_price INT,
        full_description TEXT,
        Size_Table TEXT,
        Material_Table TEXT,
        PRIMARY KEY(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS shop_list_tooling (
        id INTEGER,
        name_product TEXT,
        product_price TEXT,
        full_description TEXT,
        metal_thickness TEXT,
        PRIMARY KEY(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS other_products_list (
        id INTEGER,
        name_product TEXT,
        price INT,
        full_description TEXT,
        PRIMARY KEY(id)
    )''')
        
    conn.commit()
   








def read_sqlite_table(records,name_db):   #проверка сколько строк в таблице
    
    global numb_colums,string_db
   
    try:
        sqlite_connection = sqlite3.connect('DB/Database.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = f"""SELECT * from {name_db}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        numb_colums = len(records)
        string_db = len(records)
        return numb_colums
        

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


    
def chek_db_console():
    return "Подключен к SQLite\nВсего товаров в таблице: "+str(string_db)






def chek_db_telegram(name_db):
    conn = sqlite3.connect('DB/Database.db')
    c = conn.cursor()
    record = c.execute(f'''SELECT * FROM {name_db}''')
    items =  c.fetchall()
    list_items = []
    for i in range(len(items)):
        list_items.append(items[i][0:2])
        
    return len(items),list_items






def focus_del_item_pos(item_pos,name_db):
    
    conn = sqlite3.connect('DB/Database.db')
    c = conn.cursor()
  
    del_item_pos = c.execute(f'''DELETE FROM {name_db} WHERE ID = {item_pos};''')
    conn.commit()


def get_last_id(name_db):
    conn = sqlite3.connect('DB/Database.db')
    c = conn.cursor()
    get_last_id = c.execute(f'''SELECT MAX(`id`) FROM {name_db}''')
    id =  c.fetchall()
    int_id = id[0][0]
    if int_id == None:
        int_id = 1
    else:
        int_id += 1

    return int_id







def add_message_shop_list_table(name_product:str, price_4: int, price_5: int, price_6: int, price_8: int, price_10: int, price_12: int, assembly_price: int, full_description: str,Size_Table:str,Material_Table:str,name_db):
        
        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''INSERT INTO {name_db} (name_product,price_4, price_5, price_6, price_8, price_10, price_12, assembly_price, full_description,Size_Table,Material_Table) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (name_product,price_4, price_5, price_6, price_8, price_10, price_12, assembly_price, full_description,Size_Table,Material_Table))
        conn.commit()


def add_message_shop_list_tooling(name_product:str, product_price: str, full_description: str, metal_thickness:str, name_db):

        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''INSERT INTO {name_db} (name_product,product_price,full_description,metal_thickness) VALUES (?,?,?,?)''', (name_product,product_price,full_description,metal_thickness))
        conn.commit()
   

def add_message_shop_list_other(name_product:str, price:int, full_description: str,name_db):

        conn = create_connection()
        c = conn.cursor()
        c.execute(f'''INSERT INTO {name_db} (name_product,price,full_description) VALUES (?,?,?)''', (name_product,price,full_description))
        conn.commit()
   




def drop_db():
    conn = create_connection()
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS shop_list_tooling')
    c.execute('DROP TABLE IF EXISTS shop_list_table')
    c.execute('DROP TABLE IF EXISTS other_products_list')










   
def edit_product_all(dev_id, salary,name_db,name_column):


    sqlite_connection = create_connection()
    cursor = sqlite_connection.cursor()
    

    sql_update_query = f"""Update {name_db} set {name_column} = ? where id = ?"""
    data = (salary, dev_id)
    cursor.execute(sql_update_query, data)
    sqlite_connection.commit()
    cursor.close()







    
 #///////////////////////////////////////////////////////////// inline  
def check_db(db_name):
    conn = create_connection()
    c = conn.cursor()
    record = c.execute(f'''SELECT * FROM {db_name}''')
   
    return record,c.fetchall()




def check_db_price(name_db,item_pos,item_name):
    conn = create_connection()
    c = conn.cursor()
   
    record = c.execute(f'''SELECT {item_name} FROM {name_db} WHERE ID = {item_pos};''')
   
    return c.fetchall()[0][0]



def check_db_product_name(name_db,item_pos):
    conn = create_connection()
    c = conn.cursor()
   
    record = c.execute(f'''SELECT name_product FROM {name_db} WHERE ID = {item_pos};''')
   
    return c.fetchall()[0][0]