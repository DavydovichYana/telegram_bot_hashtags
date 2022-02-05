from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    await bot.set_webhook(config.URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()