from random import randint
import telebot

# Создаем бота, пишем свой токен
bot = telebot.TeleBot('5572182114:AAEGaREq4XiSrXJdUjxRNteu2Bd0pBD4VUM')

flag = randint(1,2)
value=2021

def answer(text):
    global flag
    global value
    try:
        k=int(text)
    except:
        return ('Введите ЧИСЛО конфет <=28')  
    if k<=28:
        if value > 28:
            if flag==1:
                value -= k
                flag = 2
                return ('Теперь число конфет вводит Игрок 2. Осталось '+str(value))
            else:
                value -= k
                flag = 1
                return ('Теперь число конфет вводит Игрок 1. Осталось '+str(value))
        if value<=28:
            if flag==1:
                value=2021
                flag = randint(1,2)
                return ('Победил Игрок 1. Начинаем сначала...Начинаем игру, у нас 2021 конфета. Начинает игрок '+str(flag)+' . Введите число конфет')
            else:
                value=2021
                flag = randint(1,2)
                return ('Победил Игрок 2. Начинаем сначала...Начинаем игру, у нас 2021 конфета. Начинает игрок '+str(flag)+' . Введите число конфет')
    else:
        return ('Введите ЧИСЛО конфет <=28')  
            
# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m):
    global flag 
    global value 
    value=2021   
    bot.send_message(m.chat.id, 'Начинаем игру, у нас 2021 конфета. Начинает игрок '+str(flag)+' . Введите число конфет')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    s=answer(message.text)
    # Отправка ответа
    bot.send_message(message.chat.id, s)
# Запускаем бота
bot.polling(none_stop=True, interval=0)