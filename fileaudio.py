from gtts import gTTS
import os

text = open("demo.txt","r",encoding='utf-8').read()
language = "hi"
output = gTTS(text=text,lang = language,slow=False)
output.save("fileout.mp3")
os.system("start fileout.mp3")