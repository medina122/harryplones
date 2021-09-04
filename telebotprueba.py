import telebot 
import logging
from telebot import apihelper
from lxml import html
import requests

chatid =  1711761717
apihelper.SESSION_TIME_TO_LIVE = 5 * 60
token = '1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg'
bot = telebot.TeleBot(token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hi, how can i help you with?")

@bot.message_handler(commands=['ID'])
def send_userID(message):
    chatid = message.chat.id
    bot.reply_to(message, 'Your ID is %s' % chatid)

@bot.message_handler(commands=['PVU'])
def PVUPrice(message):
    url = 'https://coinmarketcap.com/currencies/plantvsundead/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    Name = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/h2/text()')
    Price = tree.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/text()')
    FinalName = str(Name[-1])
    FinalPrice = str(Price[-1])
    Data = "%s price %s" % (FinalName, FinalPrice)
    bot.reply_to(message, Data)
    
bot.polling(none_stop=True)
