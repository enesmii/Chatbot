# Bot PMB
import os
from tkinter import *
from tkinter import filedialog

import aiml


root = Tk()
root.title("PMB UKDW")
root.geometry("400x470")

main_menu = Menu(root)
file_menu = Menu(root)

main_menu.add_cascade(label="File", menu=file_menu)
root.config(menu=main_menu)

# # Untuk chat area
chatWindow = Text(root, bd=1, bg="white", width=50, height=8, font="Corbel 11", fg="blue")
chatWindow.place(x=6, y=6, height=390, width=385)
#
# # Untuk message window
messageWindow = Text(root, bg="white", width=30, height=4, font="Corbel 11")
messageWindow.place(x=6, y=400, height=40, width=385)
#

#
# # Add the scroll bar
scrollbar = Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=400, y=5, height=435)
#
# root.mainloop()

# Membuat kernel dan mempelajari berkas aiml
kernel = aiml.Kernel()

# Membuat file brain untuk mempercepat learning
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="start.xml", commands="pmb")
    kernel.saveBrain("bot_brain.brn")

chatWindow.insert(END, "Aku Figo. selamat datang di chatbot PMB UKDW. \nInformasi apa yang ingin kamu ketahui?")


# Function button send
# noinspection PyShadowingNames
def sendMessage():
    send = "Pengguna  : " + messageWindow.get(1.0, END)
    user_input = kernel.respond(messageWindow.get(1.0, END))
    chatWindow.insert(END, "\n" + send)
    if user_input:
        chatWindow.insert(END, "Bot : " + user_input)
    else:
        chatWindow.insert(END, "Bot : Maaf kakak, Saya kurang mengerti")
    messageWindow.delete(1.0, END)


def saveFile():
    dir_name = filedialog.asksaveasfile()
    os.chdir(dir_name)

    curr_dir = os.getcwd()
    print(curr_dir)


# # Create the button to send the message
send = Button(root, text="Send", fg="white", bg="blue", activebackground="lightblue", width=12, height=5,
              font=("Corbel", 12), command=sendMessage)

send.place(x=300, y=400, height=40, width=85)
send.place(x=300, y=400, height=40, width=85)

root.mainloop()
