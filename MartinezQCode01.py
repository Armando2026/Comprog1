from tkinter import *
from tkinter.ttk import *
from time import strftime

top=Tk()
top.title("Digital Clock")
def none():
    text=strftime(' %H:%M:%S %p ')
    Ibl.config(text=text)
    Ibl.after(1000,none)
Ibl=Label(top,font=('digital-7' ,50,'bold'),
          background='black',foreground='red')
Ibl.pack(anchor='center')
none()
mainloop()
