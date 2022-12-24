from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
import os

API_TOKEN = "5538729980:AAH-noC1xWL1l_F3xYcMADfTSMWauOFQ_kc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

buttons = [
    [
        types.KeyboardButton(text=""),
    ],
]

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)