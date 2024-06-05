from aiogram import executor
from loader import dp
import handlers
from data import data_agent

async def on_shutdown_function(dispatcher):
    data_agent.save_data()

if __name__ == '__main__':
    executor.start_polling(dispatcher = dp, 
                           skip_updates=True, 
                           on_shutdown = on_shutdown_function)