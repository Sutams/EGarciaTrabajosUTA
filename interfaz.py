import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Window and game variables
window = Tk()

window.title("Welcome player 1 to the game Flip Tac Toe")
window.geometry("400x300")

img=PhotoImage(file="gato2.png")
lbiamgen = Label(window,image = img).place(x=-10,y=-10)
lbl = Label(window, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)