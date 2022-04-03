from pydub.playback import play
from pydub import AudioSegment
from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from speech_text import STT
import os
from io import BytesIO

dic = ('chinese', 'zh-cn', 'dutch', 'nl', 'english', 'en',
       'french', 'fr', 'german', 'de', 'italian', 'it', 'japanese', 'ja',
       'korean', 'ko', 'portuguese', 'pt', 'spanish', 'es')


# input from user
query = STT()
while (query == "None"):
    query = STT()

# enter the language to translate say "spanish", ect
# we could take this whole section out since Dr file is in english, or use it to output audio and text
# back in the original language used
""""
def destination_language():
    print("enter language")
    # input destination language
    to_lang = STT()

    while (to_lang == "None"):
        to_lang = STT()
    to_lang = to_lang.lower()
    return to_lang


to_lang = destination_language()
"""
to_lang = "english"
# mapping language with code
while (to_lang not in dic):
    print("try another language")
    #to_lang = destination_language()

to_lang = dic[dic.index(to_lang)+1]

# translate with chosen language
translator = Translator()

# translate from src to destination
text_to_translate = translator.translate(query, dest=to_lang)
# text is translated and can be fed into eliza
text = text_to_translate.text

# using google text to speech method to input translated speech to destinatin language
# stored in to_lang, 3 arg is false since its slow
speak = gTTS(text=text, lang=to_lang, slow=False)


mp3_fp = BytesIO()
speak.write_to_fp(mp3_fp)
mp3_fp.seek(0)
response = AudioSegment.from_file(mp3_fp, format="mp3")

# play(response)  # audio out

print(text)  # text out
