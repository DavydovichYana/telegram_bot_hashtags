import traceback

from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot
from key_words import rake_key
from keyboards import client_kb

answers = {}


async def start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               'Привет:) Можешь оставить свой текст здесь, а я подберу тэги для него. '
                               'Текст может быть на русском или английском языках.',
                               reply_markup=client_kb.kb_client)
        await message.delete()
    except:
        await message.reply('Сначала напиши мне в личные сообщения:)\nhttps://t.me/Pizza_Sheef_ibot')


async def who_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Я подбираю хэштэги к текстам.\nПросто отправь мне любой текст и получишь список тэгов!'
                           '\nИспользуй из для Инстаграмма, ТикТока, Вконтакте и других социальных сетей:)')
    await message.answer('⬇️Отправьте ваш текст⬇️')


async def text_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите текст 📝')


async def hashtags_command(message: types.Message):
    try:
        await message.reply(rake_key.Hashtags().all_compile(message.text))
        await message.answer('⬇️Отправьте ещё текст⬇️')

    except:
        print(traceback.format_exc())
        await message.answer('Слишком короткий текст. Не могу создать тэги:(')


async def likes_command(message: types.Message):
    await message.answer('Оцените качество хэштэгов, пожалуйста😊', reply_markup=client_kb.votes_kb)


async def vote_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answers:
        answers[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
    print(answers)


async def urls_command(message: types.Message):
    await message.reply('Хочешь узнать как я нахожу ключевые слова в твоих текстах? Смотри: ',
                        reply_markup=client_kb.url_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(text_command, lambda message: 'Ввести текст' in message.text)
    dp.register_message_handler(who_command, lambda message: 'Инструкция' in message.text)
    dp.register_message_handler(urls_command, lambda message: 'Ссылки' in message.text)
    dp.register_message_handler(likes_command, lambda message: 'Оценить ' in message.text)
    dp.register_message_handler(hashtags_command)
    dp.register_callback_query_handler(vote_call, Text(startswith='like_'))
