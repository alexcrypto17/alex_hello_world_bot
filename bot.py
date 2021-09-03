#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Лицензия: CC0

"""
Simple Bot to reply to Telegram messages.
"""
import os
from dotenv import load_dotenv

load_dotenv()

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Включаем логи (это учет о программе)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))

# Определение обработчиков телеграм команд.
# телеграм команды начинаються со слеша.
# 
# Обычно обработчики телеграм команд
# принимают два аргумента: update и
# context (cреда). В случаи ошибки внутри обработчика
# запускаеться ошибка TelegramError.
def start(update, context):
    """Отправь сообщение когда запускаеться
    команда /start или /запуск"""
    update.message.reply_text('Bot started! Бот запущен!')

def help(update, context):
    """Отправь сообщение когда запускаеться
    команда /help или /помощь"""
    update.message.reply_text('Command list:\n\
    \t/start - start this bot\n\
    \t/help - print command list\n\
    \t/author - author of this bot\n\
    \t/link - link to the source code in GitHub\n\
    \n\
    Список команд:\n\
    \t/запуск - запускаем этого бота\n\
    \t/помощь - показывает список команд\n\
    \t/автор - показывает автора этого бота\n\
    \t/ссылка - ссылка на исходный код в GitHub\n\
    ')

def author(update, context):
    """Отправь сообщение когда запускаеться
    команда /author или /автор"""
    update.message.reply_text('Alex Chan. Лонг Чан')

def link(update, context):
    """Отправь сообщение когда запускаеться
    команда /link или /ссылка"""
    update.message.reply_text('https://github.com/alexcrypto17/alex_hello_world_bot')

def echo(update, context):
    """Повторяет сообщения пользователя обратно"""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Учет ошибок вызываемий обьектом update."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Запуск бота."""
    TOKEN = os.getenv('TOKEN')
    APP_NAME = os.getenv('APP_NAME')

    # Создаем update и передаем ему токен нашего бота.
    # Учтите установить use_context=True чтобы 
    # использовать новый контекст основанный на 
    # возвращаемых функциях.
    # Версии 12 это не обьязательно
    updater = Updater(TOKEN, use_context=True)

    # Берем диспечер чтобы зарегистрировать обрабочиков 
    # команд
    dp = updater.dispatcher

    # Когда в телеграме посылаеться команда
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("author", author))
    dp.add_handler(CommandHandler("link", link))
    # Когда команды на русском языке
    # dp.add_handler(CommandHandler("запуск", start))
    # dp.add_handler(CommandHandler("помощь", help))
    # dp.add_handler(CommandHandler("автор", author))
    # dp.add_handler(CommandHandler("ссылка", link))

    # Когда в телеграме посылаеться не командное сообщение
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Запись учета всех ошибок
    dp.add_error_handler(error)

    # Следующая команда запускает бот
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Следующая команда останавливает бот безопасно
    updater.idle()

# Самостоятельный скрипт.
# Теперь этот бот можно запустить вызовом:
# python bot.py
if __name__ == '__main__':
    main()