import os
from dotenv import load_dotenv
import telebot
import speech_recognition as sr
from app import modelo_linguagem
from app import transcricao_audio
from io import BytesIO
from pydub import AudioSegment
load_dotenv()


def salvar_audio(msg):
    """Baixa o áudio do Telegram e salva localmente"""

    if msg.voice:
        file_info = bot.get_file(msg.voice.file_id)
    elif msg.audio:
        file_info = bot.get_file(msg.audio.file_id)
    
    downloaded_file = bot.download_file(file_info.file_path)

    file_name = 'audio_2.ogg'

    with open(file_name,'wb') as f:
        f.write(downloaded_file)
    
    return file_name



   
    # audio_bytes = BytesIO(downloaded_file)
    # audio = AudioSegment.from_file(audio_bytes,format="ogg")


    return audio

# def transcreve_audio(arquivo):
   
   








bot = telebot.TeleBot(os.getenv("API_KEY_TELEGRAM"))

@bot.message_handler(content_types= ['audio','voice'])

def transcreve_audio(msg: telebot.types.Message):
   
   
    file_path = salvar_audio(msg)

    with open(file_path,'rb') as f:
        transcript = transcricao_audio(f)

    texto_reposta = modelo_linguagem(transcript)

    
    bot.reply_to(msg,texto_reposta)




@bot.message_handler(content_types=['text'])
def captura_mensagem(msg: telebot.types.Message):

    

    texto = msg.text

    texto_respota = modelo_linguagem(texto)

    bot.reply_to(msg,texto_respota)


    




bot.infinity_polling()