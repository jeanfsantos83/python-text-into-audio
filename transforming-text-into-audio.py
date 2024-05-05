from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='Meu primeiro áudio gerado com Python!',
    lang=language
)

sp.save(audio)
playsound(audio)