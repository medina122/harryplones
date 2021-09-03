import telebot 

token = '1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg'
bot = telebot.TeleBot(token)
chatid =  1711761717
text1 = 'hola'
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "I'm messed up doing those stupid things but i got u back")

bot.polling()
