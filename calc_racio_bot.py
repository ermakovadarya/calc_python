import datetime
import logging
import telebot
import random
from telebot import types
import time

def calc_rac_num(bot,message):
    bot.send_message(message.chat.id, 'Введите строку для вычисления. Можно использовать операции +,-,/,*')
    time.sleep(15)
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        primer=message.text
        bot.send_message(message.chat.id, primer)
    # logging.log(primer)
    res=[]
    i=0
    while i<len(primer):      
        if primer[i]=='+' or primer[i]=='-' or primer[i]=='*' or primer[i]=='/':
            res.append(float(primer[:i]))
            res.append(primer[i])
            primer=primer[i+1:]
            i=0
        else:
            i+=1
    res.append(float(primer))

    operat={
        '+':lambda x,y:x+y,
        '*':lambda x,y:x*y,
        '-':lambda x,y:x-y,
        '/':lambda x,y:x/y
    }
    def calc(op,x,y):
        return operat[op](x,y)
    def calculation(x,y,res):   
        i=0
        while i<len(res):
            if res[i]==x or res[i]==y:
                result=calc(res[i],res[i-1],res[i+1])
                res.insert(i+2,result)
                res.pop(i+1)
                res.pop(i)
                res.pop(i-1)
                i-=2
            i+=1

    calculation('*','/',res)
    calculation('+','-',res)
            
    print(round(res[0],2))
    now=datetime.datetime.now()
    # logging.log(str(now))
    # logging.log(str(f'Рузультат = {round(res[0],2)}'))
    # logging.log('END')