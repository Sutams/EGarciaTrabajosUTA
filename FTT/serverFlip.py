import socket
import threading

from tkinter import *
from tkinter import messagebox
import tkinter

window = Tk()

cell = ""
turn = True

host = '10.90.90.93'
port = 65535

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
        cell = dataa[0]
        update()
        if dataa[1] == 'YourTurn':
            turn = True
            print("server turn = " + str(turn))


def update():
    if cell == 'A':
        clicked1()
    elif cell == 'B':
        clicked2()
    elif cell == 'C':
        clicked3()
    elif cell == 'D':
        clicked4()
    elif cell == 'E':
        clicked5()
    elif cell == 'F':
        clicked6()
    elif cell == 'G':
        clicked7()
    elif cell == 'H':
        clicked8()
    elif cell == 'I':
        clicked9()
    else:
        print("No matching char detected")


def waiting4connection():
    print("Thread created")
    global conn, addr
    conn, addr = sock.accept()
    print("Client is connected")
    recieveData()


create_thread(waiting4connection)

########################

window.title("Welcome player 1 to the game Flip Tac Toe")
window.geometry("400x300")

lbl = Label(window, text="Flip Tac Toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)


def clicked1():
    global turn
    global cell
    if turn == True and btn1["text"] == "":
        btn1["text"] = "X"
        send_data = '{}-{}'.format('A', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn1["text"] == "" and cell == 'A':
        btn1["text"] = "O"
        turn = True
        check()


def clicked2():
    global turn
    global cell
    if turn == True and btn2["text"] == "":
        btn2["text"] = "X"
        send_data = '{}-{}'.format('B', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn2["text"] == "" and cell == 'B':
        btn2["text"] = "O"
        turn = True
        check()


def clicked3():
    global turn
    global cell
    if turn == True and btn3["text"] == "":
        btn3["text"] = "X"
        send_data = '{}-{}'.format('C', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn3["text"] == "" and cell == 'C':
        btn3["text"] = "O"
        turn = True
        check()


def clicked4():
    global turn
    global cell
    if turn == True and btn4["text"] == "":
        btn4["text"] = "X"
        send_data = '{}-{}'.format('D', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn4["text"] == "" and cell == 'D':
        btn4["text"] = "O"
        turn = True
        check()


def clicked5():
    global turn
    global cell
    if turn == True and btn5["text"] == "":
        btn5["text"] = "X"
        send_data = '{}-{}'.format('E', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn5["text"] == "" and cell == 'E':
        btn5["text"] = "O"
        turn = True
        check()


def clicked6():
    global turn
    global cell

    if turn == True and btn6["text"] == "":
        btn6["text"] = "X"
        send_data = '{}-{}'.format('F', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn6["text"] == "" and cell == 'F':
        btn6["text"] = "O"
        turn = True
        check()


def clicked7():
    global turn
    global cell
    if turn == True and btn7["text"] == "":
        btn7["text"] = "X"
        send_data = '{}-{}'.format('G', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn7["text"] == "" and cell == 'G':
        btn7["text"] = "O"
        turn = True
        check()


def clicked8():
    global turn
    global cell
    if turn == True and btn8["text"] == "":
        btn8["text"] = "X"
        send_data = '{}-{}'.format('H', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn8["text"] == "" and cell == 'H':
        btn8["text"] = "O"
        turn = True
        check()


def clicked9():
    global turn
    global cell
    if turn == True and btn9["text"] == "":
        btn9["text"] = "X"
        send_data = '{}-{}'.format('I', 'YourTurn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn9["text"] == "" and cell == 'I':
        btn9["text"] = "O"
        turn = True
        check()


flag = 1


def check():
    global flag
    flag = flag + 1

    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]

# [[123],[456],[789],[147],[258],[369],[159],[357]]
    if (b1 == b2 == b3) and (b1 == "X" or b1 == "O"):
        win(btn1["text"])
    if (b4 == b5 == b6) and (b4 == "X" or b4 == "O"):
        win(btn4["text"])
    if (b7 == b8 == b9) and (b7 == "X" or b7 == "O"):
        win(btn7["text"])
    if (b1 == b4 == b7) and (b1 == "X" or b1 == "O"):
        win(btn1["text"])
    if (b2 == b5 == b8) and (b2 == "X" or b2 == "O"):
        win(btn2["text"])
    if (b3 == b6 == b9) and (b3 == "X" or b3 == "O"):
        win(btn3["text"])
    if (b1 == b5 == b9) and (b1 == "X" or b1 == "O"):
        win(btn1["text"])
    if (b3 == b5 == b7) and (b3 == "X" or b3 == "O"):
        win(btn3["text"])
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied! Try again")
        window.destroy()


def win(player):
    ans = "Game complete, player " + player + " wins"
    messagebox.showinfo("Congratulations!", ans)
    window.destroy()


btn1 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked1)
btn2 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked2)
btn3 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked3)
btn4 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked4)
btn5 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked5)
btn6 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked6)
btn7 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked7)
btn8 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked8)
btn9 = Button(window, text=None, bg="white", fg="black", width=3,
              height=1, font=('Helvetica', '20'), command=clicked9)
btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)

window.mainloop()
