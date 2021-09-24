import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

win = Tk()
buttons = []

# FUNCION QUE GENERA UNA MATRIX 3X3 DE BOTONES
# FALTA HACER QUE AL PRESIONAR EL BOTÓN, ÉSTE CAMBIE POR X u O

def clicked(i):
    buttons[i]['text']='a'

global x
x=0
for i in range (3):
    for j in range (3):
        b = Button(win, bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=clicked(x))
        x=x+1
        b.grid(row=i, column=j)
        buttons.append(b)



win.mainloop()