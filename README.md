<img src="https://png.icons8.com/color/1600/telegram-app.png" width="190" align="right">

# pyTelegramGrilletbot
A bot for telegram written in python

## Documentation

You can find more documentation `here` [Telegram Bot API for pyhton](https://github.com/eternnoir/pyTelegramBotAPI)
`and here` [Telegram Bot API](https://core.telegram.org/bots/api) and if you speack spanish `you can also see` [This video](https://www.youtube.com/watch?v=AYcO4ezgsQg&t=1s), [and this](https://www.youtube.com/watch?v=dEthunx1rUc)

## What GrilletBot can do?

* Can use ChatterBot to have a nice conversation
* Can learn conversations from multiple plain text files
* Can choise a random pic from a folder and send it when recive the `/senpicute` command
* Can even use him to find files in your pc and send it to you or anybody else you want (in progress)

## Getting started.

* First we need to download this proyect or clone it usin `git` and then install the requirements

```
$ git clone https://github.com/Grillet0xEB/pyTelegramGrilletbot.git
$ cd pyTelegramGrilletBot
$ pip install -r requirements.txt
```

* Now we run the bot with `pyhton`

```
$ python TlgGrilletBot.py
```

## How does it work?

* First we import all the libraries we'll use for this

```python
import os
import time
import random
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
```

* Set the telegram bot token to our bot. To see how we get the API token see the [documentation](#documentation)

```pyhton
bot = telebot.AsyncTeleBot(<TOKEN>)
```

* Then we create a ChatterBot and make him learn from all txt files in the folder `Conversaciones`

```python
grilletBot = ChatBot('grilletBot')
grilletBot.set_trainer(ListTrainer)
	
for archivo in os.listdir('Conversaciones'):
	chats = open('Conversaciones/' + archivo, 'r').readlines()
	grilletBot.train(chats)
```

* Now we'll create the handlers to do any thing we want, first say hi to the commands `/help` and `/start`

```python
@bot.message_handler(commands=["help", "start"])
def enviar_saludo(message):
	mensaje 	= message.text
	destinatario	= message.chat.id
	bot.reply_to(message, "Estoy listo!")
	bot.send_message(destinatario, "Hola, soy GrilletBot")
```

* Then send a random picture from the folder `Imagenes`  no matter how many pictures are in there

```python
@bot.message_handler(commands=["sendpicture"])
def enviar_nudes(message):
	mensaje 	= message.text
	destinatario 	= message.chat.id
	username 	= message.chat.username
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
```

* Now we say that send a message when he interac in a private chat and reply a message when not

```python
@bot.message_handler(func=lambda message:True)
def responder_mensaje(message):
	mensaje 	= message.text
	destinatario 	= message.chat.id
	username 	= message.chat.username
	fechaMensaje 	= message.date
	respuesta 	= str(Oreo.get_response(mensaje))
	if message.chat.type == "private":
		bot.send_chat_action(destinatario, 'typing')
		bot.send_message(destinatario, respuesta)
	else:
		bot.reply_to(message, respuesta)
```

* When we recive a voice note we'll answer it with a voice note spoken in japanese that say `Why are you sending me voice notes?`

```python
@bot.message_handler(content_types=['voice'])
def responder_notaDeVoz(message):
	destinatario  = message.chat.id
	nota = open('Voz/voz.ogg', 'rb')
	bot.send_chat_action(destinatario, 'record_audio')
	bot.send_voice(destinatario, nota, 'Escuchame')
```

* And finally we handle any other file we recive saying `What is that?`

```python
@bot.message_handler(content_types=['document', 'photo' 'audio', 'video', 'file'])
def responder_multimedia(message):
	bot.reply_to(message, 'No se que hacer con esto')
```

At the end of the code we add `bot.polling()` to start the bot

<img src="https://chatterbot.readthedocs.io/en/stable/_images/banner.png" width="550" align="left">
