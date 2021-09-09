import telebot 
import logging
import json
import requests
from telebot import apihelper

chatid =  1711761717
telebot.apihelper.SESSION_TIME_TO_LIVE = 5 * 60
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

@bot.message_handler(commands=['coins'])
def GetPrice(message):

    lista = ['bitcoin', 'ethereum', 'plant-vs-undead-token','smooth-love-potion', 'cardano', 'solana', 'litecoin', 'dogecoin', 'algorand', 'binancecoin', 'zilliqa', 'shiba-inu', 'bittorrent-2', 'terra-luna', 'mist', 'pancakeswap-token', 'matic-network']
    final = []
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=%s&vs_currencies=usd'%(ID)
    response = requests.get(url)
    jsonload = json.loads(response.text)
    price = float(jsonload[ID]["usd"])
    final.append(price)
    

    for coingeckoid in lista:
        GetPrice(coingeckoid)

    watchlist = f''' 

    Bitcoin: {final[0]}$
    Ethereum: {final[1]}$ 
    Plants vs Undead: {final[2]}$
    Smooth Love Potion: {final[3]}$
    Cardano: {final[4]}$
    Solana: {final[5]}$
    Litecoin: {final[6]}$
    Dogecoin: {final[7]}$
    Algordand: {final[8]}$
    Binance: {final[9]}$
    Zil: {final[10]}$
    Shiba: {final[11]}$
    BitTorrent: {final[12]}$
    Luna: {final[13]}$ 
    Mist: {final[14]}$
    Pankake: {final[15]}$
    Matic: {final[16]}$
    '''

    bot.reply_to(message, watchlist)

    
bot.polling(none_stop=True)


