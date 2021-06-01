from aiogram.types import Message
from aiogram_metrics import track

from bot.misc import dp


@dp.message_handler(commands=['start'])
@track('/start command')
async def handle_start(msg: Message):
    await msg.reply('Hi! Welcome!')


@dp.message_handler(commands=['help'])
@track('/help command')
async def handle_help(msg: Message):
    await msg.reply('Halp!')
