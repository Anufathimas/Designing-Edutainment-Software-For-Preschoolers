
from tkinter import *
import tkinter
import tkinter.font as font
import tkinter.messagebox

obj=tkinter.Tk()
obj.title("Login")
obj.geometry("700x500")
myFont = font.Font(family='Arial', size=30, weight='bold')
button = Button(obj, text='My Button')
#applying font to the button label
button['font'] = myFont
button.pack()

Label1 = Label(obj, text = "This is my new project in python!")
Label1['font'] = myFont
Label1.pack()

def mybuttonclick():
        tkinter.messagebox.showinfo('hello','hai')

mybutton=Button(obj,text="click me",font=("Bahnschrift",14),command =(mybuttonclick()))
mybutton.pack()

mylabel=Label(obj,text="Hello",font=("Arial",10))
mylabel.pack()

listbx=Listbox(obj)
listbx.insert(1,'my list 1')
listbx.insert(2,'my list 2')
listbx.insert(3,'my list 3')
listbx.insert(4,'my list 4')
listbx.pack()

mymsg=Menubutton(obj,text="this is menubutton",font=("Arial",10))
mymsg.pack()

myradio=Radiobutton(obj,text="option 1",value=1)
myradio.pack()

myradio1=Radiobutton(obj,text="option 2",value=2)
myradio1.pack()
obj.mainloop()

