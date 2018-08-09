from gtts import gTTS
import os
from tkinter import *

root=Tk()
root.geometry('400x200')
root.title("Google's Speech Application")
lab1=Label(root,text='Text To Speech Convertor',bg='powder blue',fg='black',font=('arial 16 bold')).pack()
root.config(background='powder blue')

lab2=Label(root,text='Enter text',font=('arial 16'),bg='powder blue',fg='black').pack()
mytext=StringVar()



def fetch():
   language='en'
   myob=gTTS(text=mytext.get(),lang=language,slow=False)
   myob.save('Voice1.mp3')

def play():
   from pygame import mixer
   mixer.init()
   mixer.music.load("Voice1.mp3")
   mixer.music.play()
   

ent1=Entry(root,tex=mytext,font=('arial 13')).pack()

but1=Button(root,text='Convert',width=20,bg='brown',fg='white',command=fetch).place(x=125,y=100)

but2=Button(root,text='Play file',width=20,bg='brown',fg='white',command=play).place(x=125,y=140)

root.mainloop()

          
