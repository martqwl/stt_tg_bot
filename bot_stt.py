from telebot import telebot
from telebot.types import Message
from validators_stt import is_stt_block_limit
from speechkit_stt import speech_to_text
from telebot.types import ReplyKeyboardMarkup
from info_stt import *
from db_stt import *
from config_stt import TOKEN
bot = telebot.TeleBot(TOKEN)

def create_keyboard(buttons_list):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons_list)
    return keyboard

@bot.message_handler(commands=['start'])
def bot_start(message):
    keyboard = create_keyboard(["/help"])
    bot.send_message(message.chat.id, text=start_message, reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def bot_help(message):
    keyboard = create_keyboard(["/start", "/help", "/stt", "/tts"])
    bot.send_message(chat_id=message.chat.id, text=help_message, reply_markup=keyboard)

# Обрабатываем команду /stt
@bot.message_handler(commands=['stt'])
def stt_handler(message: Message):
    bot.send_message(message.chat.id, "Отправьте гс")
    bot.register_next_step_handler(message, stt)


def stt(message: Message):
    user_id = message.chat.id

    # Проверка, что сообщение действительно голосовое
    if not message.voice:
        bot.send_message(message.chat.id, "Не гс!")
        return

    # Считаем аудиоблоки и проверяем сумму потраченных аудиоблоков
    stt_blocks, error_message = is_stt_block_limit(user_id, message.voice.duration)
    if not stt_blocks:
        bot.send_message(user_id, error_message)
        return


    voice_id = message.voice.file_id
    info_file = bot.get_file(voice_id)
    file = bot.download_file(info_file.file_path)

    status, message = speech_to_text(file)

    # Если статус True - отправляем текст сообщения и сохраняем в БД, иначе - сообщение об ошибке
    if status:
        insert_row(user_id, stt_blocks)
        bot.send_message(user_id, message)

if __name__ == '__main__':
    bot.infinity_polling()
    prepare_db()