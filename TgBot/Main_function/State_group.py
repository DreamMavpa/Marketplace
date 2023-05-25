from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





class Db_tooling(StatesGroup):
        price = State()
        name_towar = State()
        product_preview = State()
        product_group = State()
        short_description = State()
        full_description = State()
     


class Db_table(StatesGroup):
        price_4 = State()
        price_5 = State()
        price_6 = State()
        price_8 = State()
        price_10 = State()
        price_12 = State()
        name_towar = State()
        product_preview = State()
        product_group = State()
        short_description = State()
        full_description = State()
        Size_Table = State()
        metal_thickness_Table = State()
        Hole_diameter_Table = State()
        Material_Table = State()
        


class Db_other_product(StatesGroup):
        name_towar = State()
        description = State()
        price = State()
        product_preview = State()
        product_group = State()


#///////////////////////////////////////// edit
class edit_db(StatesGroup):
        edit_info = State()



