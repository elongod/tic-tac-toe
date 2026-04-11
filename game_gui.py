import tkinter as tk

board = [" "] * 9
current_player = "X"
score = {"X": 0, "O": 0, "平局": 0}

def click(position):
    global current_player
    if board[position] == " ":
        board[position] = current_player
        buttons[position].config(text=current_player)
        winner = check_winner()
        if winner:
            score[winner] += 1
            update_score_label()
            status_label.config(text=winner + " 獲勝！🎉")
            disable_all()
        elif " " not in board:
            score["平局"] += 1
            update_score_label()
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

def update_score_label():
    score_label.config(text=f"X: {score['X']}  平局: {score['平局']}  O: {score['O']}")

def restart():
    global current_player
    current_player = "X"
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state="normal")
    status_label.config(text="輪到 X 下棋")

def reset_score():
    score["X"] = 0
    score["O"] = 0
    score["平局"] = 0
    update_score_label()
    restart()

window = tk.Tk()
window.title("圈圈叉叉")

score_label = tk.Label(window, text="X: 0  平局: 0  O: 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3, pady=(8, 0))

buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=("Arial", 30), width=4, height=2,
                       command=lambda i=i: click(i))
    button.grid(row=(i//3)+1, column=i%3)
    buttons.append(button)

status_label = tk.Label(window, text="輪到 X 下棋", font=("Arial", 16))
status_label.grid(row=4, column=0, columnspan=3)

restart_button = tk.Button(window, text="重新開始", font=("Arial", 14), command=restart)
restart_button.grid(row=5, column=0, columnspan=2)

reset_score_button = tk.Button(window, text="重置分數", font=("Arial", 14), command=reset_score)
reset_score_button.grid(row=5, column=2)

window.mainloop()