import os
import time
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = telebot.AsyncTeleBot("459912388:AAFhawlpahUapv4hq1pOANlevp6fepwrPS8")

Oreo = ChatBot('Oreo')
Oreo.set_trainer(ListTrainer)
	
for archivo in os.listdir('Data'):
	chats = open('Data/' + archivo, 'r').readlines()
	Oreo.train(chats)

@bot.message_handler(commands=["help", "start"])
def enviar_saludo(message):
	mensaje 	  = message.text
	destinatario  = message.chat.id
	bot.reply_to(message, "Estoy listo!")
	bot.send_message(destinatario, "Hola, soy Oreo")

@bot.message_handler(func=lambda message:True)
def responder_mensaje(message):
	mensaje 	  = message.text
	destinatario  = message.chat.id
	username 	  = message.chat.username
	fechaMensaje  = message.date
	respuesta 	  = str(Oreo.get_response(mensaje))
	if message.chat.type == "private":
		bot.send_message(destinatario, respuesta)
		#print(str(time.strftime("%D %H:%M", time.localtime(fechaMensaje))) + " " + username + ": " + mensaje)
		#print("\t\t\t " + str(respuesta))
	else:
		bot.reply_to(message, respuesta)

@bot.message_handler(content_types=['document', 'photo' 'audio', 'video', 'voice', 'file'])
def responder_multimedia(message):
	bot.reply_to(message, "Que hago con esto?")

bot.polling()