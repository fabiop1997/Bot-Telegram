import os
from dotenv import load_dotenv
from groq import Groq
import telebot
from app import modelo_linguagem

load_dotenv()






bot = telebot.TeleBot(os.getenv("API_KEY_TELEGRAM"))

@bot.message_handler(content_types= ['audio','voice'])
def transcreve_audio(msg: telebot.types.Message):

    texto_respota = "isso é uma transcrição"
   
    bot.reply_to(msg,texto_respota)




@bot.message_handler(content_types=['text'])
def captura_mensagem(msg: telebot.types.Message):

    

    texto = msg.text

    texto_respota = modelo_linguagem(texto)

    bot.reply_to(msg,texto_respota)


    




bot.infinity_polling()