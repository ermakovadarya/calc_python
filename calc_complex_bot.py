import datetime
import logging
import telebot
import random
from telebot import types

# @bot.message_handler(commands=["start"])
# def start(message):
#         markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item1=types.KeyboardButton("Комплексные числа")
#         item2=types.KeyboardButton("Рациональные числа")
#         markup.add(item1)
#         markup.add(item2)
#         bot.send_message(message.chat.id, 'Выбери режим работы калькулятора',  reply_markup=markup)

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
    
#     if message.text.strip() == 'Комплексные числа' :
#         bot.send_message(message.chat.id, 'Вы выбрали режим работы с комплексными числами')
#         calc_complex_bot.calc_comp_num()
#     elif message.text.strip() == 'Рациональные числа':
#         bot.send_message(message.chat.id, 'Вы выбрали режим работы с рациональными числами')
#         calc_racio_bot.calc_rac_num()

def calc_comp_num(bot):
    print('Введите первое комплексное число в формате a+bi. Сначала а1:')
    a1=int(input())
    print('Теперь b1: ')
    b1=int(input())
    print(f'{a1} + {b1} i\n')
    print('Введите второе комплексное число в формате a+bi. Сначала а2:')
    a2=int(input())
    print('Теперь b2: ')
    b2=int(input())
    print(f'{a2} + {b2} i\n')
    print('Введите операцию для вычисления. Можно использовать операции +,-,/,*')
    math_complex=input()

    logging.log(str(f'({a1} + {b1} i) {math_complex} ({a2} + {b2} i)'))


    if math_complex=='+':
        res=a1+a2
        resi=b1+b2
    if math_complex=='-':
        res=a1-a2
        resi=b1-b2
    if math_complex=='*':
        res=a1*a2-b1*b2
        resi=a1*b2+b1*a2
    if math_complex=='/':
        res=round(float((a1*a2+b1*b2)/(a2**2+b2**2)),3)
        resi=round(float((a2*b1-a1*b2)/(a2**2+b2**2)),3)

    print(f'{a1} + {b1} i {math_complex} {a2} + {b2} i = {res} + {resi} i')
    now=datetime.datetime.now()
    logging.log(str(now))
    logging.log(str(f'Результат = {a1} + {b1} i {math_complex} {a2} + {b2} i = {res} + {resi} i'))
    logging.log('END')
