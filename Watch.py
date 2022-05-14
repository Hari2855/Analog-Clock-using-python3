from datetime import *
from tkinter import *
import calendar

root=Tk()

root.geometry("1000x300+0+0")
root.configure(background="darkblue")
root.resizable(0,0)

root.overrideredirect(1)

def start():
    dt=datetime.now()
    time=(dt.strftime("%B-%d-%Y %I:%M:%S %p"))
    label.config(text=time)
    label.after(200,start)
    

label = Label(root,font=("ds-digital",50),bg="black",fg="Blue",bd=50)
label.grid(row=0,column=1)
start()
print("Done")
root=mainloop()
