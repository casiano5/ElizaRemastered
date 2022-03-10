from googletrans import Translator
import sys

translator = Translator()

def translate(text,dest="en"):
    translation = translator.translate(text,dest)
    return translation.text

def detectlanguage(text):
    return translator.translate(text).src

print(translate(sys.argv[1], sys.argv[2]))