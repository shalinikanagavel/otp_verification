import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("350x200")
Window.title("MAIL OTP")
def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
label1=Label(Window,text="One Time Password",relief="solid",font=("arial",15,"bold"),fg='green').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="EMAIL ID",font=("arial",10,"bold")).place(x=25,y=50)
w=Entry(Window,width=20,validate="key",textvariable=a)
w.place(x=130,y=50)
log = Button(Window, text="Proceed",relief="raised", bg='red', font=("arial", 10, "bold"), fg='black',command=verify).place(x=155,y=100)
Window.mainloop()