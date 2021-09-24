import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

window=Tk()

buttons = []
cell = ''
turn = True

host = '127.0.0.1'
port = 65535

conn, addr = None, None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

def create_thread (targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def recieveData ():
    global cell
    global turn
    while True:
        data, addr = conn.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = dataa[0]
        update()
        if dataa[1]=='YourTurn':
            turn = True
            print("server turn = " + str(turn))

def update ():
    
    if cell >= 0 and cell <= 8:
        clicked(cell)
    else:
        print("No matching cell")

def clicked(btn, x):
    global turn
    global cell
    if turn == True and btn[i]["text"] == "":
        btn["text"] = "X"
        send_data = '{}-{}'.format(x,'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn["text"] == "" and cell == x:
        btn["text"] = "O"
        turn = True
        check()



flag=1
def check():
    winCond = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    flag =+ 1
    for x in winCond:
        w1, w2, w3 = x
        if (board[w1] == board[w2] == board[w3]) and (board[w1] == "X" or board[w1] == "O"):
            win(board[0])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied! Try again")
        window.destroy()

def win(player):
    ans = "Game complete, player " + player + " wins"
    messagebox.showinfo("Congratulations!", ans)
    window.destroy()

for i in range (3):
    for j in range (3):
        b = Button(window, bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'), command=clicked(buttons[i]))
        b.grid(row=i, column=j)
        buttons.append(b)

window.mainloop