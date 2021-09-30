from ctypes import sizeof
import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

# Variables del juego y la interfaz
window = Tk()
buttons = []
cell = 10
turn = True
# Verdadero significa modo Flip
gamemode = False

# Variables del servidor socket
host = '127.0.0.1'
port = 65535
# Para la conexion LAN utilizar
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


# Para estar seguro
def update():
    if cell >= 0 and cell <= 8:
        clicked(cell)
    else:
        print("No se encontró la celda")

def waiting4connection():
    print("Hilo creado")
    global conn, addr
    conn, addr = sock.accept()
    print("Cliente conectado")
    recieveData()

create_thread(waiting4connection)

# Configuracion de la ventana
window.title("Bienvenido jugador 1 al juego de Tic Tac Toe")
window.geometry("410x310")
window.resizable(width=False,height=False)

img=PhotoImage(file="gato2.png")

lbiamgen = Label(window,image = img).place(x=-10,y=-10)
label=LabelFrame(window, text="",background="#fabfbe")
label.pack(fill="none", expand="no",pady=5,padx=8)


lbl = Label(label, background="#fabfbe",text="Tic Tac Toe",fg="#62100f", font=('Helvetica', '17',"bold"))
lbl.grid(row=0, column=0)
lbl = Label(label, background="#fabfbe",text="Jugador 1: X", fg="#62100f",font=('Helvetica', '15'))

lbl.grid(row=1, column=0)
lbl = Label(label, background="#fabfbe",text="Player 2: O", fg="#62100f",font=('Helvetica', '15'))
lbl.grid(row=2, column=0)

# Funcion que imprime X u O dependiendo del boton presionado
def clicked(i):
    global turn
    global cell
    global gamemode
    if gamemode:
        if turn == True and (buttons[i]['text'] == "" or buttons[i]['text'] == "O"):
            buttons[i]['text'] = "X"
            send_data = '{}-{}'.format(i, 'YourTurn').encode()
            conn.send(send_data)
            turn = False
            check()
            cell = 10 
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

# Funcion para comprobar si alguien gano
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

# Funcion en caso de victoria
def win(player):
    ans = " player " + player + " wins"
    if(messagebox.askyesno(message= "Congratulations!" + ans + ", Play again?", title="Play again")):
        restart()
    else:
        window.destroy()
    
# Funcion de reinicio
def restart():
    global cell
    cell = 10
    for i in range(9):
        buttons[i]['text'] = ""

#Preguntar modo de juego, normal o flip
if(messagebox.askyesno(message= "Quieres jugar el modo Flip?", title="Change mode")):
    lbl = Label(label, background="#fabfbe",text="Flip Tac Toe",fg="#62100f", font=('Helvetica', '17',"bold"))
    lbl.grid(row=0, column=0)
    gamemode=True
else:
    lbl = Label(label, background="#fabfbe",text="Tic Tac Toe",fg="#62100f", font=('Helvetica', '17',"bold"))
    lbl.grid(row=0, column=0)
    gamemode=False

# Ciclo para crear botones
x = 0
for i in range(3):
    for j in range(1,4):
        
        b = Button(label, fg="black", width=3, height=1,bg="#fde8e7",activebackground="#fe7876", font=('Helvetica', '20',"bold"), command=lambda x=x: clicked(x))
        b.grid(row=i, column=j)
        buttons.append(b)
        x += 1


window.mainloop()
