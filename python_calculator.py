"""
Calculator using TKINTER

Operations: Addition, Subtraction, Multiplication, Division
Error Handling: Done
Decimal: Included
Styling: Played with colours a little
"""

# Importing packages
from tkinter import *

# GUI
window = Tk()
window.title("Python Calculator")
window.geometry("280x400")

# Input/Display field
# Entry Box
e = Entry(window, width=40, borderwidth=5, bg="WHITE", fg="BLACK")
e.place(x=10, y=0)

# Buttons
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result)+ str(num))

b1 = Button(window, text ='1', width=12, bg="BLACK", fg="WHITE", command=lambda:click(1))
b1.place(x=10, y=60)

b2 = Button(window, text ='2', width=12, bg="BLACK", fg="WHITE", command=lambda:click(2))
b2.place(x=80, y=60)

b3 = Button(window, text ='3', width=12, bg="BLACK", fg="WHITE", command=lambda:click(3))
b3.place(x=170, y=60)

b4 = Button(window, text ='4', width=12, bg="BLACK", fg="WHITE", command=lambda:click(4))
b4.place(x=10, y=120)

b5 = Button(window, text ='5', width=12, bg="BLACK", fg="WHITE", command=lambda:click(5))
b5.place(x=80, y=120)

b6 = Button(window, text ='6', width=12, bg="BLACK", fg="WHITE", command=lambda:click(6))
b6.place(x=170, y=120)

b7 = Button(window, text ='7', width=12, bg="BLACK", fg="WHITE", command=lambda:click(7))
b7.place(x=10, y=180)

b8 = Button(window, text ='8', width=12, bg="BLACK", fg="WHITE", command=lambda:click(8))
b8.place(x=80, y=180)

b9 = Button(window, text ='9', width=12, bg="BLACK", fg="WHITE", command=lambda:click(9))
b9.place(x=170, y=180)

b0 = Button(window, text ='0', width=12, bg="BLACK", fg="WHITE", command=lambda:click(0))
b0.place(x=10, y=240)

def decimal():
    result = e.get()
    if "." not in result:
        e.insert(END, ".")

b_dot = Button(window, text='.', width=12, bg="GREY", fg="WHITE", command=decimal)
b_dot.place(x=80, y=240)

# Operators
def add():
    n1 = e.get()
    if n1 == "":
        return
    global math
    global i
    math = "addition"
    i = float(n1)
    e.delete(0, END)

b_add = Button(window, text ='+', width=12, bg="GREY", fg="WHITE", command=add)
b_add.place(x=170, y=240)

def subtract():
    n1 = e.get()
    if n1 == "":
        return
    global math
    global i
    math = "subtraction"
    i = float(n1)
    e.delete(0, END)

b_sub = Button(window, text ='-', width=12, bg="GREY", fg="WHITE", command=subtract)
b_sub.place(x=10, y=300)

def multiply():
    n1 = e.get()
    if n1 == "":
        return
    global math
    global i
    math = "multiplication"
    i = float(n1)
    e.delete(0, END)

b_mul = Button(window, text ='*', width=12, bg="GREY", fg="WHITE", command=multiply)
b_mul.place(x=170, y=300)

def divide():
    n1 = e.get()
    if n1 == "":
        return
    global math
    global i
    math = "division"
    i = float(n1)
    e.delete(0, END)

b_div = Button(window, text ='/', width=12, bg="GREY", fg="WHITE", command=divide)
b_div.place(x=80, y=300)

def clear():
    e.delete(0, END)

b_clr = Button(window, text ='CLEAR', width=16, bg="RED", fg="WHITE", command=clear)
b_clr.place(x=10, y=350)

def equal():
    try:
        n2 = e.get()
        e.delete(0, END)

        if math == "addition":
            e.insert(0, i + float(n2))
        elif math == "subtraction":
            e.insert(0, i -float(n2))
        elif math == "multiplication":
            e.insert(0, i * float(n2))
        elif math == "division":
            e.insert(0, i / float(n2))

    except:
        e.insert(0, "Error")

b_eql = Button(window, text ='=', width=16, bg="GREEN", fg="WHITE", command=equal)
b_eql.place(x=140, y=350)

# End
mainloop()
