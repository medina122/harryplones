import telebot 

token = '1759121577:AAHVHZMjB8cFkxzflzcJbNz1C4vLecxzOrg'
bot = telebot.TeleBot(token)
chatid =  1711761717
text = 'hola'
bot.send_message(chat_id=chatid, text=text)
print("OK")