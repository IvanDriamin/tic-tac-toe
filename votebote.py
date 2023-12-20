import random
import telebot
#import aiogram
#from telebot import types as t
#from aiogram import Bot, Dispatcher, executor, types
TOKEN = "6823999031:AAF3VkufbyHirYfBkUu94P6N-ZxzCqD3NCk"
bot = telebot.TeleBot (TOKEN)
#bot = Bot (token = TOKEN)
#dp = Dispatcher (bot = bot)
#@dp.message_handler (command = ('start'))
@bot.message_handler (content_types = ['text'])
def gtm (message):
#async def start_ (message: types.Message):
    if message.from_user == 'Привет':
        bot.send_message ('Для того, чтобы ходить, вводите названия ячеек на английском, например: a1, b2, c3') 
        bot.send_message ('чей будет первый ход? 1 - игрок, 0 - бот')
    m = message.from_user #int (input()) #чей ход
    n = 9 #количество ходов
    a1 = ' '
    a2 = ' '
    a3 = ' '
    b1 = ' '
    b2 = ' '
    b3 = ' '
    c1 = ' '
    c2 = ' '
    c3 = ' '
    b = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'] # оставшиеся клетки
    for i in range (9):
        if m == 1:
            bot.send_message ('ход игрока')
            bot.send_message ('Введите название ячейки: ')
            if message.from_user == 'a1' and 'a1' in b:
                a1 = 'X'
                b.remove ('a1')
            if message.from_user == 'a2' and 'a2' in b:
                a2 = 'X'
                b.remove ('a2')
            if message.from_user == 'a3' and 'a3' in b:
                a3 = 'X'
                b.remove ('a3')
            if message.from_user == 'b1' and 'b1' in b:
                b1 = 'X'
                b.remove ('b1')
            if message.from_user == 'b2' and 'b2' in b:
                b2 = 'X'
                b.remove ('b2')
            if message.from_user == 'b3' and 'b3' in b:
                b3 = 'X'
                b.remove ('b3')
            if message.from_user == 'c1' and 'c1' in b:
                c1 = 'X'
                b.remove ('c1')
            if message.from_user == 'c2' and 'c2' in b:
                c2 = 'X'
                b.remove ('c2')
            if message.from_user == 'c3' and 'c3' in b:
                c3 = 'X'
                b.remove ('c3')
            if (message.from_user == 'a1' and message.from_user not in b) or (message.from_user == 'a2' and message.from_user not in b) or (message.from_user == 'a3' and message.from_user not in b) or (message.from_user == 'b1' and message.from_user not in b) or (message.from_user == 'b2' and message.from_user not in b) or (message.from_user == 'b3' and message.from_user not in b) or (message.from_user == 'c1' and message.from_user not in b) or (message.from_user == 'c2' and message.from_user not in b) or (message.from_user == 'c3' and message.from_user not in b):
                bot.send_message ('Клетка занята, штраф: игрок пропускает ход')
            if message.from_user != 'a1' and message.from_user != 'a2' and message.from_user != 'a3' and message.from_user != 'b1' and message.from_user != 'b2' and message.from_user != 'b3' and message.from_user != 'c1' and message.from_user != 'c2' and message.from_user != 'c3':
                bot.send_message ('Неправельное имя клетки, штраф: игрок пропускает ход')
            m = 0
            n -= 1
            if a1 == 'X' and a2 == 'X' and a3 == 'X':
                bot.send_message ('Игрок победил')
                break
            if b1 == 'X' and b2 == 'X' and b3 == 'X':
                bot.send_message ('Игрок победил')
                break
            if c1 == 'X' and c2 == 'X' and c3 == 'X':
                bot.send_message ('Игрок победил')
                break
            if a1 == 'X' and b1 == 'X' and c1 == 'X':
                bot.send_message ('Игрок победил')
                break
            if a2 == 'X' and b2 == 'X' and c2 == 'X':
                bot.send_message ('Игрок победил')
                break
            if a3 == 'X' and b3 == 'X' and c3 == 'X':
                bot.send_message ('Игрок победил')
                break
            if a1 == 'X' and b2 == 'X' and c3 == 'X':
                bot.send_message ('Игрок победил')
                break
            if a3 == 'X' and b2 == 'X' and c1 == 'X':
                bot.send_message ('Игрок победил')
                break
        else:
            bot.send_message ('Ход бота')
            a = random.choice (b)
            if a == 'a1':
                a1 = 'O'
                b.remove ('a1')
            if a == 'a2':
                a2 = 'O'
                b.remove ('a2')
            if a == 'a3':
                a3 = 'O'
                b.remove ('a3')
            if a == 'b1':
                b1 = 'O'
                b.remove ('b1')
            if a == 'b2':
                b2 = 'O'
                b.remove ('b2')
            if a == 'b3':
                b3 = 'O'
                b.remove ('b3')
            if a == 'c1':
                c1 = 'O'
                b.remove ('c1')
            if a == 'c2':
                c2 = 'O'
                b.remove ('c2')
            if a == 'c3':
                c3 = 'O'
                b.remove ('c3')
            m = 1
            n -= 1
            if a1 == 'O' and a2 == 'O' and a3 == 'O':
                bot.send_message ('Бот победил')
                break
            if b1 == 'O' and b2 == 'O' and b3 == 'O':
                bot.send_message ('Бот победил')
                break
            if c1 == 'O' and c2 == 'O' and c3 == 'O':
                bot.send_message ('Бот победил')
                break
            if a1 == 'O' and b1 == 'O' and c1 == 'O':
                bot.send_message ('Бот победил')
                break
            if a2 == 'O' and b2 == 'O' and c2 == 'O':
                bot.send_message ('Бот победил')
                break
            if a3 == 'O' and b3 == 'O' and c3 == 'O':
                bot.send_message ('Бот победил')
                break
            if a1 == 'O' and b2 == 'O' and c3 == 'O':
                bot.send_message ('Бот победил')
                break
            if a3 == 'O' and b2 == 'O' and c1 == 'O':
                bot.send_message ('Бот победил')
                break
        bot.send_message ("              ")
        bot.send_message ("   | A | B | C")
        bot.send_message ("___|___|___|___")
        bot.send_message ("   |   |   |")
        bot.send_message (" 3 |", a3, "|", b3, "| ", c3, "  ")
        bot.send_message ("___|___|___|___")
        bot.send_message ("   |   |   |")
        bot.send_message (" 2 |", a2, "|", b2, "| ", c2, "  ")
        bot.send_message ("___|___|___|___")
        bot.send_message ("   |   |   |")
        bot.send_message (" 1 |", a1, "|", b1, "| ", c1, "  ")
        bot.send_message ("   |   |   |")
        bot.send_message ("            ")
bot.polling(none_stop=True, interval=0)
