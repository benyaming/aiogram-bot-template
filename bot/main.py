from config import METRICS_DSN, METRICS_TABLE_NAME, WEBHOOK_PATH, IS_PROD

import aiogram_metrics
from aiogram.utils.executor import start_polling, start_webhook

import bot.handlers
from bot.misc import bot, dp, logger
from bot.middleware import sentry_context_middleware


def fix_imports():
    _ = bot.handlers = sentry_context_middleware


async def on_start(_):
    logger.info('Starting {{PROJECT NAME}} bot...')

    if METRICS_DSN:
        await aiogram_metrics.register(METRICS_DSN, METRICS_TABLE_NAME)


async def on_down(_):
    from aiogram_metrics.api import close
    await close()


if __name__ == '__main__':
    if IS_PROD:
        start_webhook(dp, WEBHOOK_PATH, on_startup=on_start)
    else:
        start_polling(dp, on_startup=on_start, skip_updates=True)
