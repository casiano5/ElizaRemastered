import json
import os.path
import tkinter
import eliza
from speech import speech


speechRunning = False
if not os.path.exists("eliconfig.json"):
    eliza_config = {
        "textToSpeechEnable": False,
        "speechToTextEnable": False,
        "speakerIconPath": "disSpeaker_Icon.png",
        "micIconPath": "disMic.png"
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
        self.speakerimage = tkinter.PhotoImage(file=eliza_config["speakerIconPath"])
        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()  # For the messages to be sent.
        self.my_msg = my_msg.get()
        #packing scrollbar and chatbox
        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        self.msg_list = msg_list
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        messages_frame.pack()


        #def getUserSpeech(event=None):




        def send_user_input(event=None):
            end = False
            or_message = my_msg.get()
            my_msg.set("")
            usermsg = "USER: " + or_message
            msg_list.insert(tkinter.END, usermsg)
            self.window.update()
            self.window.update_idletasks()
            a = eli.converse(or_message)
            if a is None:
                a = eli.final()
                end = True
            self.msg_list.insert(tkinter.END, "ELIZA: " + a)
            self.window.update()
            self.window.update_idletasks()
            if eliza_config["textToSpeechEnable"]:
                speech(a)
            if end:
                exit(0)


        def changeTTS():
            if eliza_config["textToSpeechEnable"]:
                eliza_config["speakerIconPath"] = "disSpeaker_Icon.png"
            else:
                eliza_config["speakerIconPath"] = "Speaker_Icon.png"
            self.speakerimage = tkinter.PhotoImage(file=eliza_config["speakerIconPath"])
            text_to_speech_button.config(image=self.speakerimage, width="20", height="50")
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
            speech_to_text_button.config(image=self.micimage, width="20", height="50")
            eliza_config["speechToTextEnable"] = not eliza_config["speechToTextEnable"]
            myJSON = json.dumps(eliza_config)
            with open("eliconfig.json", "w") as jsonfile:
                jsonfile.write(myJSON)

        #speech to text
        speech_to_text_button = tkinter.Button(command=changeSTT)
        speech_to_text_button.config(image=self.micimage, width="20", height="20")
        speech_to_text_button.pack(side=tkinter.RIGHT)
        # text_to_speech_button
        text_to_speech_button = tkinter.Button(command=changeTTS)
        text_to_speech_button.config(image=self.speakerimage, width="20", height="20")
        text_to_speech_button.pack(side=tkinter.LEFT)
        # input box
        entry_field = tkinter.Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", send_user_input)
        entry_field.pack(side=tkinter.LEFT)
        # send button
        send_button = tkinter.Button(top, text="Send", command=send_user_input)
        send_button.config()
        send_button.pack()
        msg_list.insert(tkinter.END, "ELIZA: How do you do? Please tell me your problem")
        self.window.update()
        self.window.update_idletasks()
        if eliza_config["textToSpeechEnable"]:
            speech("How do you do? Please tell me your problem")


EGUI = GUI()
EGUI.window.mainloop()
EGUI.window.update_idletasks()
