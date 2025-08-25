import os
from dotenv import load_dotenv
from groq import Groq
import telebot
from app import modelo_linguagem

load_dotenv()






bot = telebot.TeleBot(os.getenv("API_KEY_TELEGRAM"))

@bot.message_handler(func=lambda msg:True)


def captura_mensagem(msg: telebot.types.Message):
    texto = msg.text

    texto_respota = modelo_linguagem(texto)

    bot.reply_to(None,texto_respota)


    




bot.infinity_polling()