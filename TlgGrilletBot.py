import os
import time
import random
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = telebot.AsyncTeleBot(<TOKEN>)

grilletBot = ChatBot('grilletBot')
grilletBot.set_trainer(ListTrainer)
	
for archivo in os.listdir('Conversaciones'):
	chats = open('Conversaciones/' + archivo, 'r').readlines()
	grilletBot.train(chats)

@bot.message_handler(commands=["help", "start"])
def enviar_saludo(message):
	mensaje 		= message.text
	destinatario	= message.chat.id
	bot.reply_to(message, "Estoy listo!")
	bot.send_message(destinatario, "Hola, soy GrilletBot")

@bot.message_handler(commands=["sendpicture"])
def enviar_nudes(message):
	mensaje 		= message.text
	destinatario 	= message.chat.id
	username 		= message.chat.username
	fechaMensaje 	= message.date
	numero = random.randint(1, len(os.listdir('Imagenes')))
	contador = 1
	for archivo in os.listdir('Imagenes'):
		if contador == numero:
			foto = open('Imagenes/' + archivo, 'rb')
			bot.send_chat_action(destinatario, 'upload_photo')
			bot.send_photo(destinatario, foto)
			break
		contador += 1

@bot.message_handler(func=lambda message:True)
def responder_mensaje(message):
	mensaje 		= message.text
	destinatario 	= message.chat.id
	username 		= message.chat.username
	fechaMensaje 	= message.date
	respuesta 		= str(Oreo.get_response(mensaje))
	if message.chat.type == "private":
		bot.send_chat_action(destinatario, 'typing')
		bot.send_message(destinatario, respuesta)
	else:
		bot.reply_to(message, respuesta)

@bot.message_handler(content_types=['voice'])
def responder_notaDeVoz(message):
	destinatario  = message.chat.id
	nota = open('Voice/voz.ogg', 'rb')
	bot.send_chat_action(destinatario, 'record_audio')
	bot.send_voice(destinatario, nota, 'Escuchame')

@bot.message_handler(content_types=['document', 'photo' 'audio', 'video', 'file'])
def responder_multimedia(message):
	bot.reply_to(message, 'No se que hacer con esto')

bot.polling()
