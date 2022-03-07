import json
import os.path
import tkinter
import eliza
import speech_text
import translate
from speech import speech
from speech_text import STT


speechRunning = False
supported_langs_dict = translate.lang_Compatability()
# create a dict with language names as keys and locales as values
reversed_langs_dict = {value: key for (key, value) in supported_langs_dict.items()}
supported_langs = list(supported_langs_dict.values())

if not os.path.exists("eliconfig.json"):
    eliza_config = {
        "textToSpeechEnable": False,
        "speechToTextEnable": False,
        "speakerIconPath": "disSpeaker_Icon.png",
        "micIconPath": "disMic.png",
        "language": "en"
    }
    myJSON = json.dumps(eliza_config)

    with open("eliconfig.json", "w") as jsonfile:
        jsonfile.write(myJSON)
else:
    with open("eliconfig.json", "r") as jsonfile:
        eliza_config = json.load(jsonfile)
eli = eliza.Eliza()
eli.load("doctor.txt")


class GUI:
    def __init__(self):

        top = tkinter.Tk()
        top.title("Eliza")
        self.window = top
        self.micimage = tkinter.PhotoImage(file=eliza_config["micIconPath"])
        self.speakerimage = tkinter.PhotoImage(
            file=eliza_config["speakerIconPath"])
        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()  # For the messages to be sent.
        self.my_msg = my_msg.get()
        # packing scrollbar and chatbox
        # To navigate through past messages.
        scrollbar = tkinter.Scrollbar(messages_frame)
        msg_list = tkinter.Listbox(
            messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        self.msg_list = msg_list
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        messages_frame.pack()




        def send_user_input(event=None):
            end = False
            or_message = my_msg.get()
            msg_to_eng = translate.translate(or_message, dest="en")
            print(f"Message to English: {msg_to_eng}")
            my_msg.set("")
            usermsg = "USER: " + or_message
            msg_list.insert(tkinter.END, usermsg)
            self.window.update()
            self.window.update_idletasks()
            a = eli.converse(msg_to_eng)
            if a is None:
                a = eli.final()
                end = True
            if eliza_config["language"] != "en":
                a = translate.translate(a, dest=eliza_config["language"])
            self.msg_list.insert(tkinter.END, "ELIZA: " + a)
            self.window.update()
            self.window.update_idletasks()
            if eliza_config["textToSpeechEnable"]:
                speech(a, eliza_config["language"])
            if end:
                exit(0)

        def changeTTS():
            if eliza_config["textToSpeechEnable"]:
                eliza_config["speakerIconPath"] = "disSpeaker_Icon.png"
            else:
                eliza_config["speakerIconPath"] = "Speaker_Icon.png"
            self.speakerimage = tkinter.PhotoImage(file=eliza_config["speakerIconPath"])
            text_to_speech_button.config(image=self.speakerimage, width="20", height="20")
            eliza_config["textToSpeechEnable"] = not eliza_config["textToSpeechEnable"]
            myJSON = json.dumps(eliza_config)
            with open("eliconfig.json", "w") as jsonfile:
                jsonfile.write(myJSON)

        def changeSTT():
            if eliza_config["speechToTextEnable"]:
                eliza_config["micIconPath"] = "disMic.png"
            else:
                eliza_config["micIconPath"] = "mic.png"
            self.micimage = tkinter.PhotoImage(file=eliza_config["micIconPath"])
            speech_to_text_button.config(image=self.micimage, width="20", height="20")
            eliza_config["speechToTextEnable"] = not eliza_config["speechToTextEnable"]
            self.window.update()
            self.window.update_idletasks()

        def getUserSpeech():
            changeSTT()
            my_msg.set(STT(language=eliza_config["language"]))
            self.window.update()
            self.window.update_idletasks
            changeSTT()

                
        # speech to text

        speech_to_text_button = tkinter.Button(command=getUserSpeech)
        speech_to_text_button.config(
            image=self.micimage, width="20", height="20")
        speech_to_text_button.pack(side=tkinter.RIGHT)


        # text_to_speech_button
        text_to_speech_button = tkinter.Button(command=changeTTS)
        text_to_speech_button.config(
            image=self.speakerimage, width="20", height="20")
        text_to_speech_button.pack(side=tkinter.LEFT)
        # input box
        entry_field = tkinter.Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", send_user_input)
        entry_field.config(width="38")
        entry_field.pack(side=tkinter.LEFT)
        # send button
        send_button = tkinter.Button(top, text="Send", command=send_user_input)
        send_button.config(width="5", height="1")
        send_button.pack()

        # language dropdown

        drop_string = tkinter.StringVar()
        drop_string.set(supported_langs_dict[eliza_config["language"]])


        def change_language(self):
            choice = drop_string.get()
            print(choice)
            if reversed_langs_dict[choice] != eliza_config["language"]:
                eliza_config["language"] = reversed_langs_dict[choice]
                myJSON = json.dumps(eliza_config)
                with open("eliconfig.json", "w") as jsonfile:
                    jsonfile.write(myJSON)

        dropdown = tkinter.OptionMenu(
            top,
            drop_string,
            *supported_langs,
            command=change_language
        )

        # positioning widget
        dropdown.pack(expand=True)

        greet_msg = "How do you do? Please tell me your problem"
        print(f'Language upon startup: {eliza_config["language"]}')
        if eliza_config["language"] != "en":
            greet_msg = translate.translate(greet_msg, dest=eliza_config["language"])
        msg_list.insert(
            tkinter.END, "ELIZA: " + greet_msg)
        self.window.update()
        self.window.update_idletasks()
        if eliza_config["textToSpeechEnable"]:
            speech(greet_msg, eliza_config["language"])

            
EGUI = GUI()
EGUI.window.mainloop()
EGUI.window.update_idletasks()

