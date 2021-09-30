import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Window and game variables
window = Tk()
buttons = []
cell = 10
turn = False
gamemode = False

# Socket server variables
host = '127.0.0.1'
port = 65535
# For LAN connection use the following
# host = '10.90.90.93'
# port = 65535

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((host, port))
connected = False
while not connected:
    try:
        sock.connect((host,port))
        connected = True
    except Exception as e:
        pass #Do nothing, just try again

# Function to make sure
def update():
    if cell >= 0 and cell <= 8:
        clicked(cell)
    else:
        print("No matching cell")

def create_thread(targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True
    thread.start()

def recieveData():
    global cell
    global turn
    while True:
        data, addr = sock.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = int(dataa[0])
        update()
        if dataa[1] == 'YourTurn':
            turn = True

create_thread(recieveData)

# Window config
window.title("Welcome player 2 to the game Flip Tac Toe")
window.geometry("420x320")
window.resizable(width=False,height=False)

img=PhotoImage(file="raton2.png")
lbiamgen = Label(window,image = img).place(x=-10,y=-10)

label=LabelFrame(window, text="",background="#bec4fa")
label.pack(fill="none", expand="no",pady=5,padx=8)

lbl = Label(label, bg="#bec4fa", text="Flip Tac Toe Game",fg="#0a1685", font=('Helvetica', '17',"bold"))
lbl.grid(row=0, column=0)
lbl = Label(label,bg="#bec4fa", text="Player 1: X", fg="#0a1685",font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(label,bg="#bec4fa", text="Player 2: O", fg="#0a1685",font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

# Function to print X or O in case of button clicked
def clicked(i):
    global turn
    global cell
    global gamemode
    if gamemode:
        if turn == True and (buttons[i]['text'] == "" or buttons[i]['text'] == "X"):
            buttons[i]['text'] = "O"
            send_data = '{}-{}'.format(i, 'YourTurn').encode()
            sock.send(send_data)
            turn = False
            cell = 10
            check()
        elif turn == False and (buttons[i]['text'] == "" or buttons[i]['text'] == "O")  and cell == i:
            buttons[i]['text'] = "X"
            turn = True
            check()
    else:
        if turn == True and buttons[i]['text'] == "":
            buttons[i]['text'] = "O"
            send_data = '{}-{}'.format(i, 'YourTurn').encode()
            sock.send(send_data)
            turn = False
            check()
        elif turn == False and buttons[i]['text'] == "" and cell == i:
            buttons[i]['text'] = "X"
            turn = True
            check()
    print(turn)

# Function to check if the game is over
def check():
    winCond = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]    
    for item in winCond:
        w1, w2, w3 = item
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

#Ask gamemode
if(messagebox.askyesno(message= "Quieres jugar el modo Flip?", title="Change mode")):
    gamemode=True
else:
    gamemode=False

# Loop to create buttons
x = 0
for i in range(3):
    for j in range(1,4):        
        b = Button(label, bg="#dee1fc", fg="black", width=3, height=1,activebackground="#4153fb", font=('Helvetica', '20',"bold"), command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1

window.mainloop()
