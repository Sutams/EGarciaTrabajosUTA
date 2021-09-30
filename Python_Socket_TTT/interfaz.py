import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Window and game variables
window = Tk()
buttons= []
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

labelframe = LabelFrame(window, text="")
labelframe.pack(fill="none", expand="yes",pady=10)
 
left = Label(labelframe, text="")
left.place(x= 30, y=30)

img=PhotoImage(file="gato2.png")
lbiamgen = Label(labelframe,image = img)
lbl = Label(labelframe, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(labelframe, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(labelframe, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

lbl = Label(labelframe, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.place()

# Loop to create buttons
x = 0
for i in range(3):
    for j in range(1,4):
        b = Button(labelframe, bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1
window.mainloop()