import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


def modelo_linguagem(msg):

    cliente = Groq(

        api_key=os.getenv("API_KEY"),

    )

    chat_completion = cliente.chat.completions.create(

        model = "llama-3.3-70b-versatile",

        messages = [{"role":"system","content":"Você é um assistende de dúvidas, responda de forma cordial e curta"},
                    {"role":"user","content": msg}],
        temperature=0.6,
        max_tokens=300
     

    )

    return  chat_completion.choices[0].message.content


def transcricao_audio(arquivo):
      
    cliente = Groq(

            api_key=os.getenv("API_KEY"),

        )
    transcript = cliente.audio.transcriptions.create(
                
                file= arquivo,
                model = "whisper-large-v3",
                language="pt",
                temperature=0.0,
                response_format='text'
                

            )

    return transcript




