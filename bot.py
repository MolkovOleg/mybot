import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

PROXY = {'proxy_url': settings.PROXY_URL,
        'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

logging.basicConfig(filename="bot.log", level=logging.INFO, encoding='utf-8')

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")  # Текст выводимый ботом в клиенте

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    # Создание бота и передача ему ключа авторизации на сервере Telegram
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher  # Сокращение для удобства
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    logging.info("Бот стартовал...")
    # Просим бота ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота. Он работает пока мы его не остановим принудительно
    mybot.idle()

if __name__ == '__main__':
    main()