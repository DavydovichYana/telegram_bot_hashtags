import os
from aiogram.utils import executor
from create_bot import dp, on_startup, on_shutdown
from handlers import client

client.register_handlers_client(dp)
executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000))
)
