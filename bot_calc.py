import telebot
import random
from telebot import types
import calc_complex_bot
import calc_racio_bot
import datetime
import logging_bot



bot = telebot.TeleBot('5753546186:AAFvg2Edzbi1tWIVM77ODwWOF0Yv6mkeHaQ')

@bot.message_handler(commands=["start"])
def start(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Комплексные числа")
        item2=types.KeyboardButton("Рациональные числа")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id, 'Выбери режим работы калькулятора',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    
    if message.text.strip() == 'Комплексные числа' :
        bot.send_message(message.chat.id, 'Вы выбрали режим работы с комплексными числами')
        calc_complex_bot.calc_comp_num(bot)
    elif message.text.strip() == 'Рациональные числа':
        bot.send_message(message.chat.id, 'Вы выбрали режим работы с рациональными числами')
        calc_racio_bot.calc_rac_num(bot,message)

bot.polling()