import tkinter as tk

board = [" "] * 9
current_player = "X"

def click(position):
    global current_player
    if board[position] == " ":
        board[position] = current_player
        buttons[position].config(text=current_player)
        winner = check_winner()
        if winner:
            status_label.config(text=winner + " 獲勝！🎉")
            disable_all()
        elif " " not in board:
            status_label.config(text="平局！")
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
            status_label.config(text="輪到 " + current_player + " 下棋")

def check_winner():
    wins = [[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def disable_all():
    for button in buttons:
        button.config(state="disabled")

def restart():
    global current_player
    current_player = "X"
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state="normal")
    status_label.config(text="輪到 X 下棋")

window = tk.Tk()
window.title("圈圈叉叉")

buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=("Arial", 30), width=4, height=2,
                       command=lambda i=i: click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

status_label = tk.Label(window, text="輪到 X 下棋", font=("Arial", 16))
status_label.grid(row=3, column=0, columnspan=3)

restart_button = tk.Button(window, text="重新開始", font=("Arial", 14), command=restart)
restart_button.grid(row=4, column=0, columnspan=3)

window.mainloop()