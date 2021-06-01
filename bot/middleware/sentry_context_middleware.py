import sentry_sdk
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

from bot.misc import dp
from bot.config import SENTRY_PUBLIC_KEY


class SentryContextMiddleware(BaseMiddleware):

    @staticmethod
    async def on_pre_process_update(update: Update, data: dict):
        if (not update.message) and (not update.callback_query):
            return

        sentry_sdk.set_user({
            'id': (update.message or update.callback_query).from_user.id,
            'update': update.to_python()
        })


if SENTRY_PUBLIC_KEY:
    sentry_sdk.init(dsn=SENTRY_PUBLIC_KEY, integrations=[AioHttpIntegration()])
    dp.middleware.setup(SentryContextMiddleware())
