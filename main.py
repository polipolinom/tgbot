from random import random, randint
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import tempfile
import asyncio
import lorem
import json

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

buttons = [
    [
        types.KeyboardButton(text="Random wikipedia page"),
    ],
    [
        types.KeyboardButton(text="Random cat image"),
        types.KeyboardButton(text="Random number"),
    ],
    [
        types.KeyboardButton(text="Random emoji"),
        types.KeyboardButton(text="Random file"),
    ]
]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons)
    await message.reply("This is a bot that gives out a bit of random content", reply_markup=keyboard)

@dp.message_handler(commands=['creator'])
async def send_creator(message: types.Message):
    await message.reply("Polina Shaydurova, 211 group")

@dp.message_handler(commands=['wiki'])
async def send_wiki(message: types.Message):
    await get_random_wiki(message)

@dp.message_handler(commands=['cat'])
async def send_cat(message: types.Message):
    await get_random_cat(message)

@dp.message_handler(commands=['file'])
async def send_file(message: types.Message):
    await get_random_file(message)

@dp.message_handler(commands=['number'])
async def send_number(message: types.Message):
    await get_random_number(message)

@dp.message_handler(commands=['emoji'])
async def send_emoji(message: types.Message):
    await get_random_emoji(message)

async def get_random_wiki(message: types.Message):
    proc = await asyncio.create_subprocess_exec(
        'curl', '-L', 'https://en.wikipedia.org/api/rest_v1/page/random/summary',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    url =  json.loads(stdout)["content_urls"]["desktop"]["page"]
    #resp = await http3.AsyncClient().get("https://en.wikipedia.org/wiki/Special:Random")
    await message.reply(url)

async def get_random_number(message: types.Message):
    await message.reply(str(random() * randint(-108090874, 108090874)))

async def get_random_cat(message: types.Message):
    proc = await asyncio.create_subprocess_exec(
        'curl', '-L', 'https://some-random-api.ml/img/cat',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    #await message.reply(stdout)
    url = json.loads(stdout)["link"]
    #resp = await http3.AsyncClient().get('')
    await message.reply_photo(url)

async def get_random_emoji(message: types.Message):
    await message.reply(chr(0x1F600 + randint(0, 79)))

async def get_random_file(message: types.Message):
    with tempfile.TemporaryDirectory() as td:
        fname = os.path.join(td, "YourRandomFile.txt")
        with open(fname, 'w') as fh:
            fh.write(lorem.paragraph())
        await message.reply_document(open(fname, "r"), caption="Here you are")


@dp.message_handler()
async def select_distribution(message: types.Message):
    if message.text == "Random wikipedia page":
        await get_random_wiki(message)
    elif message.text == "Random number":
        await get_random_number(message)
    elif message.text == "Random cat image":
        await get_random_cat(message)
    elif message.text == "Random emoji":
        await get_random_emoji(message)
    elif message.text == "Random file":
        await get_random_file(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)