from tkinter import *
from tkinter import ttk
Win=Tk()
Win.geometry("600x600")
Win.title("Translator")
Win.configure(background="skyblue")
a=Label(Win,text="Translator").grid(row=0,column=0)
text=Text(Win,bg="white")
text.grid(row=1,column=0,columnspan=1)
a=Entry(Win,width=100)
a.grid(row=2,column=0)
def translate():
    from googletrans import Translator
    input=a.get()
    translator=Translator() 
    translated=translator.translate(input,dest='hi',src='auto')
    text.insert(END,translated.text)
T=Button(Win,text="translate",bg="pink",width=20,command=translate).grid(row=3,column=0)
Win.mainloop()
