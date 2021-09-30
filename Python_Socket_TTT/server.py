import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Window and game variables
window = Tk()
buttons = []
cell = 10
turn = True
flip = False

# Socket server variables
host = '127.0.0.1'
port = 65535
# For LAN connection use the following
# host = '10.90.90.93'
# port = 65535

conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

def create_thread(targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def recieveData():
    global cell
    global turn
    while True:
        data, addr = conn.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = int(dataa[0])
        update()
        if dataa[1] == 'YourTurn':
            turn = True
        else:
            turn = False

# Function to make sure
def update():
    if cell >= 0 and cell <= 8:
        clicked(cell)
    else:
        print("No matching cell")

def waiting4connection():
    print("Thread created")
    global conn, addr
    conn, addr = sock.accept()
    print("Client is connected")
    recieveData()

create_thread(waiting4connection)

# Window config
window.title("Welcome player 1 to the game Flip Tac Toe")
window.geometry("400x300")

img=PhotoImage(file="gato2.png")

lbiamgen = Label(window,image = img).place(x=-10,y=-10)
lbl = Label(window, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0, padx=10 ,pady=10)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

# Function to print X or O in case of button clicked
def clicked(i):
    global turn
    global cell
    global flip
    if flip:
        if turn == True and (buttons[i]['text'] == "" or buttons[i]['text'] == "O"):
            buttons[i]['text'] = "X"
            send_data = '{}-{}'.format(i, 'YourTurn').encode()
            conn.send(send_data)
            turn = False
            check()
        elif turn == False and (buttons[i]['text'] == "" or buttons[i]['text'] == "X")  and cell == i:
            buttons[i]['text'] = "O"
            turn = True
            check()
    else:
        if turn == True and buttons[i]['text'] == "":
            buttons[i]['text'] = "X"
            send_data = '{}-{}'.format(i, 'YourTurn').encode()
            conn.send(send_data)
            turn = False
            check()
        elif turn == False and buttons[i]['text'] == "" and cell == i:
            buttons[i]['text'] = "O"
            turn = True
            check()

    

# Function to check if the game is over
def check():
    winCond = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in winCond:
        w1, w2, w3 = x
        if (buttons[w1]['text'] == buttons[w2]['text'] == buttons[w3]['text']) and (buttons[w1]['text'] == "X" or buttons[w1]['text'] == "O"):
            win(buttons[w1]['text'])
    flag = 0
    for i in range(9):
        if buttons[i]['text'] != "":
            flag += 1
    if flag == 9:
        if(messagebox.askyesno(message="Match tied! try Again?", title="Second Chance")):
            restart()
        else:
            window.destroy()

# Function to tell which player won
def win(player):
    ans = " player " + player + " wins"
    if(messagebox.askyesno(message= "Congratulations!" + ans + ", Play again?", title="Play again")):
        restart()
    else:
        window.destroy()
    
# Restart or Quit function
def restart():
    global cell
    cell = 10
    for i in range(9):
        buttons[i]['text'] = ""

#Ask mode
if(messagebox.askyesno(message= "Quieres jugar el modo Flip?", title="Change mode")):
    flip=True
else:
    flip=False

# Loop to create buttons
x = 0
for i in range(3):
    for j in range(1,4):
        b = Button(window, bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1

window.mainloop()
