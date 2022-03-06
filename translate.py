''' 
requries googletrans ==3.1.0a0 
'''
from googletrans import Translator
from googletrans import LANGUAGES
import gtts

translator = Translator()
def translate(text,dest="en"):
    translation = translator.translate(text,dest)
    return translation.text


    
def lang_Compatability():
    supportedLangs = {}
    transDict = LANGUAGES
    ttsDict = gtts.lang.tts_langs()
    for key in transDict.keys():
        for key2 in ttsDict.keys():
            if (key.lower() == key2.lower()):
                supportedLangs[key2]= ttsDict[key2]
    
    return supportedLangs

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
                

if __name__ == "__main__":
    print(translate("Bonsoir, sava bien?"))
    print(lang_Compatability())
    print("\n")
    print(naturalSoundingLangs())
        
    
