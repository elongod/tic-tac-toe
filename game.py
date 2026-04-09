board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def draw_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_winner():
    # 橫的
    if board[0] == board[1] == board[2] != " ": return board[0]
    if board[3] == board[4] == board[5] != " ": return board[3]
    if board[6] == board[7] == board[8] != " ": return board[6]
    # 直的
    if board[0] == board[3] == board[6] != " ": return board[0]
    if board[1] == board[4] == board[7] != " ": return board[1]
    if board[2] == board[5] == board[8] != " ": return board[2]
    # 斜的
    if board[0] == board[4] == board[8] != " ": return board[0]
    if board[2] == board[4] == board[6] != " ": return board[2]
    return None

def play():
    current_player = "X"
    for turn in range(9):
        draw_board()
        print("輪到 " + current_player + " 下棋")
        while True:
                    position = int(input("選擇位置 (1-9)：")) - 1
                    if 0 <= position <= 8 and board[position] == " ":
                        board[position] = current_player
                        break
                    else:
                        print("這個位置不能下！請重新選擇。")
        winner = check_winner()
        if winner:
            draw_board()
            print(winner + " 獲勝！🎉")
            return
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    draw_board()
    print("平局！")

play()