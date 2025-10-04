import tkinter
from tkinter import messagebox
from collections import deque
game_over = False
playerX = "X"
playerO = "O"
cur_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
count = 0
queue = deque([])
def click(row, column):
    global count
    if game_over:
        return
    if board[row][column]["text"] != "":
        return
    global cur_player
    board[row][column]["text"] = cur_player
    queue.append([row, column])
    #print(queue)
    count += 1
    #print(count)
    if count % 3 == 0:
        curlist = queue.popleft()
        board[curlist[0]][curlist[1]]["text"] = ""



    if cur_player == playerX:
        cur_player = playerO
    else:
        cur_player = playerX
    label_text_var.set(f"The {cur_player}'s turn")
    checkWinner()
    if game_over:
        if cur_player == playerX:
            winner = playerO
        else:
            winner = playerX
        messagebox.showinfo("Game Over", f"The winner is {winner}")

def checkWinner():
    global game_over,count
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != ""):
        board[0][0].config(background="yellow", foreground="yellow")
        board[1][1].config(background="yellow", foreground="yellow")
        board[2][2].config(background="yellow", foreground="yellow")
        game_over = True
        count = 0
        return
    elif (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != ""):
        board[0][2].config(background="yellow", foreground="yellow")
        board[1][1].config(background="yellow", foreground="yellow")
        board[2][0].config(background="yellow", foreground="yellow")
        game_over = True
        count = 0
        return
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            game_over = True
            count = 0
            for column in range(3):
                board[row][column].config(background="yellow", foreground="yellow")
            return
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] != "":
            game_over =  True
            count = 0
            for row in range(3):
                board[row][column].config(background="yellow", foreground="yellow")
            return
    return

def restart():
    global cur_player, game_over, count, queue
    for row in range(3):
        for column in range(3):
            board[row][column]["text"] = ""
            board[row][column].config(background="grey", foreground="blue")
    cur_player = playerX
    label_text_var.set(f"The {cur_player}'s turn")
    game_over = False
    count = 0
    queue = deque([])

window = tkinter.Tk()
window.title("My first game")
#window.resizable(False, False)

label_text_var = tkinter.StringVar()
label_text_var.set(f"The {cur_player}'s turn")

frame = tkinter.Frame(window)
label = tkinter.Label(frame, textvariable=label_text_var, font=("Times New Roman", 20),
                     background="#343434", foreground="white")
label.grid(row=0, column=0, columnspan="3")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text="",font=("Arial Bold", 50, "bold"),
                                            background="grey", foreground="blue", width=4, height=2,
                                            command = lambda row=row, column=column: click(row, column))
        board[row][column].grid(row=row+1, column=column)
button = tkinter.Button(frame, text="Restart", font=("Times New Roman", 20),
                     background="#343434", foreground="black", command=restart)
button.grid(row=4, column=0, columnspan="3", sticky="WE")

frame.pack()

window.mainloop()

