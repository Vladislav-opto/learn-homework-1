"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging, ephem, settings, datetime
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def planets_const(update, context):
    user_text = update.message.text
    today = date.today().strftime('%Y/%M%D')
    dict_planets = {
          'Mars': ephem.Mars(today),
          'Mercury': ephem.Mercury(today),
          'Venus': ephem.Venus(today),
          'Jupiter': ephem.Jupiter(today),
          'Saturn': ephem.Saturn(today),
          'Neptune': ephem.Neptune(today),
          'Uranus': ephem.Uranus(today),
          'Pluto': ephem.Pluto(today),
          'Sun': ephem.Sun(today),
          'Moon': ephem.Moon(today),
    }
    if user_text.split()[1] in dict_planets:
        result = ephem.constellation(dict_planets[user_text.split()[1]])
        update.message.reply_text(f'{user_text.split()[1]} сегодня находится в созвездии {result}')
    else:
        update.message.reply_text('Такой планеты не существует!')


def ephem_bot():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets_const))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    ephem_bot()