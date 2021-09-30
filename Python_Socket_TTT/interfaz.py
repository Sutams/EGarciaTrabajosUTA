import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Window and game variables
window = Tk()
flip = False

def changeMode(modoFlip):
    global flip
    if modoFlip:
        flip=True
    else:
        flip=False
    print(flip)



window.title("Welcome player 1 to the game Flip Tac Toe")
window.geometry("400x300")
labelframe = LabelFrame(window, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="Inside the LabelFrame")
left.place(x= 30, y=30)

img=PhotoImage(file="gato2.png")
lbiamgen = Label(labelframe,image = img)


lbl = Label(labelframe, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.place()
window.mainloop()