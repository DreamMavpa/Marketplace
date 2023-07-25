from aiogram import *
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton




def menu_frep():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Добавить объявления")
    keyboard.row("Просмотреть активные объявления")
    keyboard.row("Редактировать объявления")
    keyboard.row("Удалить объявления")
    return keyboard



def cancellation():
    cancellation = ReplyKeyboardMarkup(resize_keyboard=True)
    cancellation.row("Отмена")
    return cancellation



cancellation_buttons = ['Отмена']
keyboard_cancellation = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_cancellation.add(*cancellation_buttons)




def keyboard_btn_photo():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Создать объявление")
    keyboard.row("Отмена")
    return keyboard