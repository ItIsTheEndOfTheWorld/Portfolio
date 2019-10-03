# ttt.py
#SOURCE: https://github.com/bennett39/ttt-medium/blob/master/ttt.py


def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    is_x = True
    game_over = False
    print_board(board)
    while not game_over:
        try:
            selection = convert_selection(select_square())
            place_piece(selection, is_x, board)
        except ValueError:
            print("Sorry, please select a square 1-9 that is unoccupied.")
            continue
        game_over = is_win(board) or is_draw(board)
        print_board(board)
        board = computer(board)
        game_over = is_win(board) or is_draw(board)

def convert_selection(selection):
    selection -= 1
    return (selection // 3, selection % 3)


def is_draw(board):
    for row in board:
        for val in row:
            if val == "_":
                return False
    print_board(board)
    print("Draw! No more moves!")
    return True


def is_win(board):
    winner = None
    for i in range(3):
        # horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # diagonal
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
            or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(winner + " is the winner!")
        return True
    return False


def place_piece(selection, is_x, board):
    i, j = selection
    if board[i][j] == "_":
        board[i][j] = "X" if is_x else "O"
    else:
        raise ValueError


def print_board(board):
    for row in board:
        print(row)


def select_square():
    selection = int(input("Select a square: "))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection

if __name__ == "__main__":
    main()
    
def computer(board):
    coor = [0,0]
    for x in range(0,3):
        for y in range(0,3):
            if board[x][y] == "_":
                coor = [x,y]
                break
    place_piece(coor, False, board)
    print("---------------")
    print_board(board)
    return board