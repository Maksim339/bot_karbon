from aiogram import types


def inline():
    inlinekey1 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Да',
                                       callback_data='yes')
    but_2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
    inlinekey1.add(but_1)
    inlinekey1.add(but_2)
    return inlinekey1


def inline1():
    inlinekey1 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Ок',
                                       callback_data='yes')
    but_2 = types.InlineKeyboardButton(text='Нет графика', callback_data='no')
    inlinekey1.add(but_1)
    inlinekey1.add(but_2)
    return inlinekey1
