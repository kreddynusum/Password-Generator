import string
import random
from tkinter import *
window=Tk()
e2=Entry(window)
e2.grid(row=0,column=1)
lable=Label(window,text="length:")
lable.grid(row=0,column=0)
lable1=Label(window,text="")
lable1.grid(row=1,column=0,columnspan=2)
button=Button(window,text='generate',command=lambda:text())
def password():
    if len(list(e2.get()))==0:
        lable1.config(text="please give length")
        exit
    else:
     n=int(e2.get())
     a=''
     p=[*string.digits]+[*string.ascii_letters]+[*string.punctuation]
     while True:
        a+=random.choice(p)
        if len(a)==n:
            break
     return a
def text():
    b=password()
    lable1.config(text="the password is:"+b)
button1=Button(window,text="clear",command=lambda:clear())
button1.grid(row=3,column=1)
def clear():
    lable1.config(text="the password is:")
    e2.delete(0,END)
button.grid(row=2,column=1)
mainloop()

