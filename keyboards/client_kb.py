from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# инлайн клавиатура для голосования
votes_kb = InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='1️⃣',callback_data='like_1'),
                                                 InlineKeyboardButton(text='2️⃣',callback_data='like_2'),
                                                 InlineKeyboardButton(text='3️⃣', callback_data='like_3'),
                                                 InlineKeyboardButton(text='4️⃣', callback_data='like_4'),
                                                 InlineKeyboardButton(text='5️⃣',callback_data='like_5')
                                                 )
# реплай клавиатура
b1 = KeyboardButton('Ввести текст 🖌')
b2 = KeyboardButton('Инструкция 🔍')
b3 = KeyboardButton('Ссылки 🎓')
b4 = KeyboardButton('Оценить 😎')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)

kb_client.row(b1,b2).row(b3,b4)


# инлайн клавиатура ссылочек
url_kb = InlineKeyboardMarkup(row_width=2)
url_button1 = InlineKeyboardButton(text='💁🏻‍♀️natasha для Python',url='https://github.com/natasha/natasha')
url_button2 = InlineKeyboardButton(text='🙆🏼‍♀️rutermextract для Python',url='https://github.com/igor-shevchenko/rutermextract')
url_button3 = InlineKeyboardButton(text='🙋🏽‍♀️rake-nltk для Python',url='https://github.com/csurfer/rake-nltk')
url_kb.add(url_button1).add(url_button2).add(url_button3)
