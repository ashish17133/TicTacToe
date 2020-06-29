import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
import random as rd
win=tk.Tk()
win.title("Criss Cross Game")
win.geometry("480x410+400+200")



def user():
    if (r==0):
        lab1=tk.Label(win,text="USER 1",fg="RED",bg="GREEN")
        lab1.grid(row=0,column=4,ipadx=20,ipady=20,rowspan=2,padx=20)
    else:
        lab1=tk.Label(win,text="USER 2",fg="RED",bg="GREEN")
        lab1.grid(row=0, column=4, ipadx=20, ipady=20, rowspan=2, padx=20)
r=rd.randint(0,1)
#button1
user()
def act1():
    global r
    print (r)
    if (r==0):
        r=1
        print(r)
        btn1.configure(text="X")
        
    else:
        r=0
        print(r)
        btn1.configure(text="O")
    user()


btn1=tk.Button(win,text="",command=lambda : act1())
btn1.grid(row=0,column=0,ipadx=50,ipady=50,padx=3,pady=3)

#button2
def act2():
    global r
    print(r)
    if (r==0):
        r=1
        print(r)
        btn2.configure(text="X")

    else:
        r=0
        print(r)
        btn2.configure(text="O")
    user()
btn2=tk.Button(win,text="",command=lambda : act2())
btn2.grid(row=0,column=1,ipadx=50,ipady=50,padx=3,pady=3)

#BUTTON3
def act3():
    global r
    if (r==0):
        btn3.configure(text="X")
        r=1
    else:
        btn3.configure(text="O")
        r=0
    user()
btn3=tk.Button(win,text="",command=lambda : act3())
btn3.grid(row=0,column=2,ipadx=50,ipady=50,padx=3,pady=3)

#BUTTON4
def act4():
    global r
    if (r==0):
        btn4.configure(text="X")
        r=1
    else:
        btn4.configure(text="O")
        r=0
    user()

btn4=tk.Button(win,text="",command=lambda : act4())
btn4.grid(row=1,column=0,ipadx=50,ipady=50,padx=3,pady=3)

#BUTTON5
def act5():
    global r
    if (r==0):
        btn5.configure(text="X")
        r=1
    else:
        btn5.configure(text="O")
        r=0
    user()
btn5=tk.Button(win,text="",command=lambda : act5())
btn5.grid(row=1,column=1,ipadx=50,ipady=50,padx=3,pady=3)
#BUTTON6
def act6():
    global r
    if (r==0):
        btn6.configure(text="X")
        r=1
    else:
        btn6.configure(text="O")
        r=0
    user()

btn6=tk.Button(win,text="",command=lambda : act6())
btn6.grid(row=1,column=2,ipadx=50,ipady=50,padx=3,pady=3)

#BUTTON7
def act7():
    global r
    if (r==0):
        btn7.configure(text="X")
        r=1
    else:
        btn7.configure(text="O")
        r=0
    user()
btn7=tk.Button(win,text="",command=lambda : act7())
btn7.grid(row=2,column=0,ipadx=50,ipady=50,padx=3,pady=3)
#BUtton 8
def act8():
    global r
    if (r==0):
        btn8.configure(text="X")
        r=1
    else:
        btn8.configure(text="O")
        r=0
    user()

btn8=tk.Button(win,text="",command=lambda : act8())
btn8.grid(row=2,column=1,ipadx=50,ipady=50,padx=3,pady=3)
#BUTTON 9
def act9():
    global r
    if (r==0):
        btn9.configure(text="X")
        r=1
    else:
        btn9.configure(text="O")
        r=0
    user()


btn9=tk.Button(win,text="",command=lambda : act9())
btn9.grid(row=2,column=2,ipadx=50,ipady=50,padx=3,pady=3)



win.mainloop()
