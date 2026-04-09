board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def draw_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def play():
    current_player = "X"
    for turn in range(9):
        draw_board()
        print("輪到 " + current_player + " 下棋")
        position = int(input("選擇位置 (1-9)：")) - 1
        board[position] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    draw_board()

play()