''' 
requries googletrans ==3.1.0a0 
'''
from googletrans import Translator
from googletrans import LANGUAGES


translator = Translator()
def translate(text,dest="en"):
    translation = translator.translate(text,dest)
    return translation.text
def detect(text):
    detection = translator.detect(text)
    return detection.lang

def naturalSoundingLangs():
    langs = {
        "en":"English",
        "fr":"French",
        "it":"Italian",
        "ja":"Japanese",
        "nl":"Dutch",
        "es":"Spanish",
        "ko":"Korean",
        "pt":"Portugese",
        "zh":"Chinese (Mandarin)",
        "hi":"Hindi",
        "de":"German"

    }
    return langs


        
    
