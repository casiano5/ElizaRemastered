from googletrans import Translator

translator = Translator()

def translate(text,dest="en"):
    translation = translator.translate(text,dest)
    return translation.text

def detectlanguage(text):
    return translator.translate(text).src
