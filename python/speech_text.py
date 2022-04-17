import speech_recognition as sr

def STT(file="empty", language="en"):
    # attempt to initializ the recognizerqu
    r = sr.Recognizer()
    # if no file path is given
    if (file == "empty"):
        with sr.Microphone() as source:
            # read audio data from microphone
            audio_data = r.record(source, duration=3)
        # convert speech to text
        # recoginize() will throw code if api unreachable
        try:
            # using google to translate speech file to text
            text = r.recognize_google(audio_data, language=language)
        except:
            text = r.recognize_google(audio_data)
        return text
    else:
        # if file path is passed, use the file
        with sr.AudioFile(file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
    return text
