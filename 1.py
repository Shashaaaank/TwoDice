import random
from tkinter import *

face=Tk()
face.geometry("700x450")

l1=Label(face,font=("cascadia code",200))
def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1=Button(face,text="roll the dice",command=roll)
b1.place(x=320,y=0)

face.mainloop()