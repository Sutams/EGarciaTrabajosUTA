import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

window = Tk()
buttons = []


window.title("Welcome player 1 to the game Flip Tac Toe")
window.geometry("500x500")

lbl = Label(window, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)


x = 0
for i in range(3):
    for j in range(3):
        b = Button(window, bg="white", fg="black", width=3, height=1, font=(
            'Helvetica', '20'))#, command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1


window.mainloop()
