import tkinter
import eliza

eli = eliza.Eliza()
eli.load("doctor.txt")

class GUI:
    def __init__(self, msg):
        self.msg = msg


        top = tkinter.Tk()
        top.title("Eliza")
        self.window = top
        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()  # For the messages to be sent.
        self.my_msg = my_msg.get()

        scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        self.msg_list = msg_list
        def send_eliza_response(self, output):
            output = "ELIZA: " + output
            msg_list.insert(tkinter.END, output)

        def send_user_input(event=None):
            or_message = my_msg.get()
            my_msg.set("")
            usermsg = "USER: " + or_message
            msg_list.insert(tkinter.END, usermsg)
            self.window.update()
            self.window.update_idletasks()
            a = eli.converse(or_message)
            self.msg_list.insert(tkinter.END, "ELIZA: " + a)
            self.window.update()
            self.window.update_idletasks()


        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        msg_list.pack()
        messages_frame.pack()

        entry_field = tkinter.Entry(top, textvariable=my_msg)
        entry_field.bind("<Return>", send_user_input)
        entry_field.pack()
        send_button = tkinter.Button(top, text="Send", command=send_user_input)
        send_button.pack()

