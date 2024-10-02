import config
import asyncio
from random import choice

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)



# Handle '/start' and '/help'
@bot.message_handler(commands=['start','Hello'])
async def send_welcome(message):
    text = 'Привет!, Я телеграм бот.\nЕсли нужна помошь напиши команду /help!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
async def send_welcom(message):
    text = '''Все команды бота:
    /coin подбрасывает монетку.
    /start
    /info
    '''
    await bot.reply_to(message, text)

@bot.message_handler(commands=['info', 'info1'])
async def send_welcom(message):
    text = 'Привет!, Это бот его зовут Tema!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())