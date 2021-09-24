import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

window = Tk()
buttons = []

def clicked(i):
    global turn
    global cell


x = 0
for i in range(3):
    for j in range(3):
        b = Button(window, bg="white", fg="black", width=3, height=1, font=(
            'Helvetica', '20'), command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1


window.mainloop()