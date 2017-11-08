#telepot library
import telepot 

#method to connect your bot from your token 
bot = telepot.Bot("463791509:AAH_naZeg_zYzzn_tIgioayaWsBCKBqJX20")


#A function who get the message and return to your terminal 
def recebendoMsg(msg):
	chat_id = msg['chat']['id']
	texto = 'Ola, '+msg['from']['first_name']+'!'
	bot.sendMessage(chat_id, texto)

#print(msg['text'])

#Every time someone text to the bot refreshing the function sending a new message.   
bot.message_loop(recebendoMsg)


while True:
	pass


#This python file get a mesage send for your bot and return that message on temrminal
 