from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp

from data import data_agent
from keyboard.command_buttons import *

import random
    


@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    if data_agent.check_reg(message.from_user.id):
        await message.answer(f"Привет, {message.from_user.first_name}\nСчет: {data_agent.data_dict[str(message.from_user.id)]['score']}\nПродолжим игру?",
                             reply_markup=start_keyboard)
    else:
        await message.answer(f"Привет, {message.from_user.first_name}.\nЯ - бот для игры в BlackJack.\nИгра ведется только на внутреигровые очки, но если проиграешь все, то будешь пытаться отыгрывать долги, так что играй вдумчиво и осторожно. \nНачнем игру?",
                             reply_markup=start_keyboard)



@dp.callback_query_handler(text="start_game")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    user_raund_score = 0
    bot_raund_score = 0
    user_hand: list[str] = list()
    bot_hand: list[str] = list()
    deck = [
        '2♦️', '2♣️', '2♠️', '2♥️', '3♦️', '3♣️', '3♠️', '3♥️', '4♦️', '4♣️', '4♠️', '4♥️', '5♦️', '5♣️', '5♠️', '5♥️', '6♦️', '6♣️', '6♠️', '6♥️', '7♦️', '7♣️', '7♠️', '7♥️', '8♦️', '8♣️', '8♠️', '8♥️', '9♦️', '9♣️', '9♠️', '9♥️', '10♦️', '10♣️', '10♠️', '10♥️', 'J♦️', 'J♣️', 'J♠️', 'J♥️', 'Q♦️', 'Q♣️', 'Q♠️', 'Q♥️', 'K♦️', 'K♣️', 'K♠️', 'K♥️', 'A♦️', 'A♣️', 'A♠️', 'A♥️'
    ]
    random.shuffle(deck)
    user_hand.append(deck.pop())
    bot_hand.append(deck.pop())
    if bot_hand[-1][:-2].isdigit(): bot_raund_score += int(bot_hand[-1][:-2])
    if bot_hand[-1][:-2] in ["J", "Q", "K"]: bot_raund_score += 10
    if bot_hand[-1][:-2] == "A": bot_raund_score += 11
    if user_hand[-1][:-2].isdigit(): user_raund_score += int(user_hand[-1][:-2])
    if user_hand[-1][:-2] in ["J", "Q", "K"]: user_raund_score += 10
    await state.update_data(
        user_hand = user_hand, 
        user_raund_score = user_raund_score,
        bot_hand = bot_hand, 
        bot_raund_score = bot_raund_score,
        deck = deck
    )
    if user_hand[-1][:-2] == "A":
        await call.message.answer(f"Тебе в руку пришел Туз {user_hand[-1][-2:]}!\nВыбери его вес",
                                  reply_markup=ace_keyboard)
        return None
    await call.message.answer(f"Твоя рука:\n{'    '.join(user_hand)}\nВес твоей руки: {user_raund_score}\n\nРука диллера:\n{'    '.join(bot_hand)}\nВес руки диллера: {bot_raund_score}",
                              reply_markup=play_keyboard)



@dp.callback_query_handler(text="game_more")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    game_data = await state.get_data()
    
    if len(game_data["deck"]) > 0:

        game_data["user_hand"].append(game_data["deck"].pop())
        
        if game_data["user_hand"][-1][:-2].isdigit(): game_data["user_raund_score"] += int(game_data["user_hand"][-1][:-2])
        if game_data["user_hand"][-1][:-2] in ["J", "Q", "K"]: game_data["user_raund_score"] += 10
        if game_data["user_hand"][-1][:-2] == "A":
            
            await call.message.answer(f"Тебе в руку пришел Туз {game_data['user_hand'][-1][-2:]}!\nВыбери его вес",
                                      reply_markup=ace_keyboard)
            await state.set_data(game_data)
            
            return None
        
        if game_data["user_raund_score"] > 21:
            await call.message.answer(f"Перебор = Проигрышь = -50 очков...\nТвоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}/21",
                                      reply_markup=restart_keyboard)
            data_agent.data_dict[str(call.from_user.id)]["score"] -= 50
            return None
        
        await call.message.answer(f"Твоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}\n\nРука диллера:\n{'    '.join(game_data['bot_hand'])}\nВес руки диллера: {game_data['bot_raund_score']}",
                              reply_markup=play_keyboard)
    
    await state.set_data(game_data)



@dp.callback_query_handler(text="ace_11")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    game_data = await state.get_data()
    
    game_data["user_raund_score"] += 11
    await call.message.answer(f"Твоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}\n\nРука диллера:\n{'    '.join(game_data['bot_hand'])}\nВес руки диллера: {game_data['bot_raund_score']}",
                              reply_markup=play_keyboard)
    await state.set_data(game_data)
    if game_data["user_raund_score"] > 21:
            await call.message.answer(f"Перебор = Проигрышь = -50 очков...\nТвоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}/21",
                                      reply_markup=restart_keyboard)
            data_agent.data_dict[str(call.from_user.id)]["score"] -= 50
            return None



@dp.callback_query_handler(text="ace_1")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    game_data = await state.get_data()
    
    game_data["user_raund_score"] += 1
    await call.message.answer(f"Твоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}\n\nРука диллера:\n{'    '.join(game_data['bot_hand'])}\nВес руки диллера: {game_data['bot_raund_score']}",
                              reply_markup=play_keyboard)
    await state.set_data(game_data)
    if game_data["user_raund_score"] > 21:
            await call.message.answer(f"Перебор = Проигрышь = -50 очков...\nТвоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}/21",
                                      reply_markup=restart_keyboard)
            data_agent.data_dict[str(call.from_user.id)]["score"] -= 50
            return None
    

    
@dp.callback_query_handler(text="game_end")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    game_data = await state.get_data()
    
    while game_data["bot_raund_score"] <= game_data["user_raund_score"] and game_data["bot_raund_score"] < 21:
        game_data["bot_hand"].append(game_data["deck"].pop())
        if game_data["bot_hand"][-1][:-2].isdigit(): game_data["bot_raund_score"] += int(game_data["bot_hand"][-1][:-2])
        if game_data["bot_hand"][-1][:-2] in ["J", "Q", "K"]: game_data["bot_raund_score"] += 10
        if game_data["bot_hand"][-1][:-2] == "A": 
            if game_data["bot_raund_score"] + 11 > 21: game_data["bot_raund_score"] += 1
            else: game_data["bot_raund_score"] += 11
    
    if game_data["bot_raund_score"] > game_data["user_raund_score"] and game_data["bot_raund_score"] <= 21:
        await call.message.answer(f"Ты проиграл, бот оказался удачливее.\nТвоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}\n\nРука диллера:\n{'    '.join(game_data['bot_hand'])}\nВес руки диллера: {game_data['bot_raund_score']}\nНаказание: -50 очков",
        reply_markup=restart_keyboard)
        data_agent.data_dict[str(call.from_user.id)]["score"] -= 50
        return None
    else:
        await call.message.answer(f"Ты выиграл, сегодня удача на твоей стороне.\nТвоя рука:\n{'    '.join(game_data['user_hand'])}\nВес твоей руки: {game_data['user_raund_score']}\n\nРука диллера:\n{'    '.join(game_data['bot_hand'])}\nВес руки диллера: {game_data['bot_raund_score']}\n\nНаграда: 100 очков!",
        reply_markup=restart_keyboard)
        data_agent.data_dict[str(call.from_user.id)]["score"] += 100



@dp.callback_query_handler(text="get_stat")
async def some_callback_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Счет: {data_agent.data_dict[str(call.from_user.id)]['score']}\nПродолжим игру?", 
                              reply_markup=restart_keyboard)