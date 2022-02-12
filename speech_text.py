import speech_recognition as sr

def STT():

        filename = "speechfile.wav"

        #attempt to initializ the recognizerqu
        r = sr.Recognizer()

        with sr.Microphone() as source:
        #read audio data from microphone
                print('start talking')
                audio_data = r.record(source, duration=3)
             #   print("Im thinking...")
        #convert speech to text

        #recoginize() will throw code if api unreachable

        try:
            #using google to translate speech file to text
            text= r.recognize_google(audio_data)
            print('converting audo to text...')
           # print(text)
        except:
            print('Sorry.. try agian I stupid')
        text = r.recognize_google(audio_data)
       # print(text)
        return text
