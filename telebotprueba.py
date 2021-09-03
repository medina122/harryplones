import telebot 
import logging
from telebot import apihelper

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
    
bot.polling()
