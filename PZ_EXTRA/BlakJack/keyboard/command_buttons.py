from aiogram import types

start_keyboard = types.InlineKeyboardMarkup(row_width=1)
start_keyboard.add(
    types.InlineKeyboardButton(text="Раздавай карты", 
                               callback_data="start_game")
)

play_keyboard = types.InlineKeyboardMarkup(row_width=1)
play_keyboard.add(
    types.InlineKeyboardButton(text="Еще", 
                               callback_data="game_more"),
    types.InlineKeyboardButton(text="Хватит", 
                               callback_data="game_end")
)

ace_keyboard = types.InlineKeyboardMarkup(row_width=1)
ace_keyboard.add(
    types.InlineKeyboardButton("11", callback_data="ace_11"),
    types.InlineKeyboardButton("1", callback_data="ace_1")
)

restart_keyboard = types.InlineKeyboardMarkup(row_width=1)
restart_keyboard.add(
    types.InlineKeyboardButton("Раздавай еще", 
                               callback_data="start_game"),
    types.InlineKeyboardButton("Просмотреть очки", 
                               callback_data="get_stat")
)