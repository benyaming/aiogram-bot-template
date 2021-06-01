import asyncio

import betterlogging as bl
from aiogram import Bot, Dispatcher, types

from .config import BOT_TOKEN


logger = bl.getLogger('my_bot')

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, loop, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
