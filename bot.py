from telebot import TeleBot, types
from bot_films.parser import parse_data
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    # Клавиатура
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton("🎬 Боевик"),
        types.KeyboardButton("😂 Комедия"),
        types.KeyboardButton("😱 Ужасы"),
        types.KeyboardButton("🎭 Драма"),
        types.KeyboardButton("🧠 Фантастика")
    )

    bot.send_photo(message.chat.id, open('image.jpg', 'rb'))
    bot.send_message(
        message.chat.id,
        'Ընտրիր ժանրը ես կուղարկեմ այդ ժանրի լավագույն ֆիլմերը',
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda message: True)
def handle_category(message):
    if message.text == "🎬 Боевик":
        text = parse_data('action')
        bot.send_message(message.chat.id, f"🔥 Лучшие боевики:\n{text}")

    elif message.text == "😂 Комедия":
        text = parse_data('comedy')
        bot.send_message(message.chat.id, f"😂 Лучшие комедии:\n{text}")

    elif message.text == "😱 Ужасы":
        text = parse_data('horror')
        bot.send_message(message.chat.id, f"😱 Лучшие ужасы:\n{text}")

    elif message.text == "🎭 Драма":
        text = parse_data('drama')
        bot.send_message(message.chat.id, f"🎭 Лучшие драмы:\n{text}")

    elif message.text == "🧠 Фантастика":
        text = parse_data('fantasy')
        bot.send_message(message.chat.id, f"🧠 Лучшая фантастика:\n{text}")


bot.polling()
