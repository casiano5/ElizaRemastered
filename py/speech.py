import gtts
from playsound import playsound
from io import BytesIO
import sys

def speech(input, language='en'):
    text = input    
    #request to google translate to get synthesis
    tts= gtts.gTTS(text=text, lang=language, slow=False)
    #convert to object
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    #play it
    from pydub import AudioSegment
    from pydub.playback import play
    response=AudioSegment.from_file(mp3_fp, format ="mp3")
    play(response)
    
speech(sys.argv[1], sys.argv[2])

