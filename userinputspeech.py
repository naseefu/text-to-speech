from gtts import gTTS
import os
from tkinter import *

a = Tk()

canvas = Canvas(a,width=400,height=300)
canvas.pack()

def textspeech():
    text = entry.get()
    output = gTTS(text=text,lang="en",slow=False)
    output.save('user.mp3')
    os.system("start user.mp3")

entry = Entry(a)

canvas.create_window(200,180,window=entry)

button = Button(a,text="start",command=textspeech)

canvas.create_window(200,230,window=button)

a.mainloop()