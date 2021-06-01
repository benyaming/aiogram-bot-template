import sentry_sdk
from aiogram.types import User
from aiogram_metrics import track

from bot.misc import dp, bot, logger
from bot.config import SENTRY_PUBLIC_KEY


@dp.errors_handler(exception=Exception)
@track('Error occurred')
async def main_errors_handler(_, e: Exception):
    user = User.get_current()
    await bot.send_message(user.id, f'En error occurred: {repr(e)}')
    logger.exception(e)

    if SENTRY_PUBLIC_KEY:
        sentry_sdk.capture_exception(e)
    return True
