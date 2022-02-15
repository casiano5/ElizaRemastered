import speech_recognition as sr


def STT():

    filename = "speechfile.wav"

    # attempt to initializ the recognizerqu
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read audio data from microphone
        print('start talking')
        audio_data = r.record(source, duration=3)

    # convert speech to text
    # recoginize() will throw code if api unreachable

    try:
        # using google to translate speech file to text
        text = r.recognize_google(audio_data)
        print('converting audo to text...')
    except:
        print('Sorry.. network problems? Try agian')
    text = r.recognize_google(audio_data)

    return text
