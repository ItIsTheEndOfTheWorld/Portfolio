#Kylee Willis
#7.5.21

#Battleship

import random

import sys
try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Please use IDLE - sorry!")
'''The five lines of code above are found here:
    https://stackoverflow.com/questions/42472958/how-do-i-print-colored-text-in-idles-terminal
    '''

#Create an exeception to be used in placing down ships
class RepeatLoop(Exception):
    pass


def main_menu():
    print("\n\nWelcome to Battleship! Please select an option to get started.\n")
    while True:
        #color.write gives colored text. I want things to stand out.
        color.write('{:^60s}\n'.format("Start"), "STRING")
        color.write('{:^60s}\n'.format("Rules"), "STRING")
        color.write('{:^59s}\n'.format("Quit"), "STRING")

        choice = input("\nEnter choice: ").lower().strip()

        #Validate input. If it passes, take appropriate action.
        if choice not in ["start", 'rules', 'quit']:
            color.write("\tPlease enter a valid option.\n\n", "KEYWORD")
        elif choice == "start":
            while True:
                start()
                replay = input("Would you like to play again? (y/n) ").lower().strip()
                if replay != "y" and replay != "yes":
                    print("Goodbye!")
                    break
            break
        elif choice == "rules":
            rules()
            break
        else:
            print("Goodbye!")
            break



def start():
    #Generate boards for playing.
    user = [[0]*8 for x in range(8)]
    cpu_visible = [[0]*8 for x in range(8)]
    cpu_hidden = [[0]*8 for x in range(8)]

    #Ask the user if they want to manually place ships or not. Take appropriate
    #   action
    own_gen = ""
    while True:
        print("Would you like to place your own ships or randomly generate positions?")
        own_gen = input("\tType either \"place\" or \"generate\": ").strip().lower()
        if own_gen in ["place", "generate"]:
            break
        color.write("\tInvalid input.\n", "KEYWORD")
    if own_gen == "place":
        user = get_coordinates(user, "battleship")
        user = get_coordinates(user, "destroyer")
        user = get_coordinates(user, "patrol boat")
    else:
        user = generate_board(user)

    #Generate CPU board
    cpu_hidden = generate_board(cpu_hidden)

    #Start game!
    color.write("\n\nGAME START\n", "KEYWORD")
    while True:
        #Print the current state of the boards
        print_board(cpu_visible, "Computer")
        print_board(user, "User")

        #Allow the user to attack. See if they've won.
        attack(cpu_visible, cpu_hidden)
        u_win = check_win(cpu_visible, cpu_hidden)
        if u_win == 1:
            color.write("\tYou win!\n\n", "STRING")
            break

        #Allow the computer to attack. See if it's won.
        cpu_attack(user)
        c_win = check_win(user)
        if c_win == 1:
            color.write("\tYou lost.\n\n", "STRING")
            break


def get_coordinates(board, ship):
    LETTERS = "abcdefgh"
    NUMBERS = "12345678"

    #Get ship size based on passed ship type.
    size = 0
    if ship == "battleship":
        size = 4
    else:
        size = 3 if ship == "destroyer" else 2

    while True:
        #Print user's board. Get coordinates they'd like to place a ship at.
        print_board(board, "User")
        print("\nType the coordinates you would like your %s to start at." % ship)
        coor = input("\t(Format: letter number) ").lower().strip().split()

        #Validate input. Get orientation if it passes.
        if coor[0] in LETTERS and coor[1] in NUMBERS:
            ori = input("How would you like your %s oriented? (north/east/south/west) " % ship).lower().strip()

            #Validate input. Attempt to fill those positions on the board.
            #   If attempt fails, RepeatLoop exception will be raised.
            if ori in ["north", "east", "south", "west"]:
                try:
                    board = fill_board(board, coor[0], coor[1], size, ori)
                    break
                except RepeatLoop:
                    continue

            else:
                color.write("\tThat is not a valid orientation. Please reenter coordinates.\n", "KEYWORD")
        else:
            color.write("\tCoordinates are invalid. Please try again.\n", "KEYWORD")
    return board


def fill_board(user, letter, number, size, orient):
    LET_NUM = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    ORI_NUM = {'north': -2, 'west': -1, 'east': 1, 'south': 2}

    #Convert input into usable data
    row = int(number) - 1
    col = LET_NUM[letter]
    ori = ORI_NUM[orient]

    #Verify that the ship wouldn't go out of bounds.
    if ori == -2 and row-size-1 < 0: #north
        color.write("\tNot enough squares that direction. Please reenter coordinates.\n", "KEYWORD")
        raise RepeatLoop
    elif ori == -1 and col-size-1 < 0: #west
        color.write("\tNot enough squares that direction. Please reenter coordinates.\n", "KEYWORD")
        raise RepeatLoop
    elif ori == 1 and col+size-1 > 7: #east
        color.write("\tNot enough squares that direction. Please reenter coordinates.\n", "KEYWORD")
        raise RepeatLoop
    elif ori == 2 and row+size-1 > 7: #south
        color.write("\tNot enough squares that direction. Please reenter coordinates.\n", "KEYWORD")
        raise RepeatLoop

    #Verify that the squares the ship would take up are empty.
    for x in range(size):
        if ori == -2 and user[row-x][col] != 0: #north
            color.write("\tSquare is already filled. Please reenter coordinates.\n", "KEYWORD")
            raise RepeatLoop
        elif ori == -1 and user[row][col-x] != 0: #west
            color.write("\tSquare is already filled. Please reenter coordinates.\n", "KEYWORD")
            raise RepeatLoop
        elif ori == 1 and user[row][col+x] != 0: #east
            color.write("\tSquare is already filled. Please reenter coordinates.\n", "KEYWORD")
            raise RepeatLoop
        elif ori == 2 and user[row+x][col] != 0: #south
            color.write("\tSquare is already filled. Please reenter coordinates.\n", "KEYWORD")
            raise RepeatLoop

    #Fill squares.
    for x in range(size):
        if ori == -2: #north
            user[row-x][col] = '|'
        elif ori == -1: #west
            user[row][col-x] = '-'
        elif ori == 1: #east
            user[row][col+x] = '-'
        else: #south
            user[row+x][col] = '|'

    return user


def generate_board(board):
    size = 2
    while size < 5:
        #Randomly generate positions of ships.
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        poss_ori = []

        #Determine how the ships can sit. Not complex - if there's less than 4
        #   spaces in one direction, it can't lay that way.
        if row < 4:
            poss_ori += [2] #south
        else:
            poss_ori += [-2] #north
        if col < 4:
            poss_ori += [1] #east
        else:
            poss_ori += [-1] #west
        ori = random.choice(poss_ori)

        #Check to make sure the squares aren't filled.
        filled = 0
        for x in range(size):
            if ori == -2 and board[row-x][col] != 0: #north
                filled = 1
            elif ori == -1 and board[row][col-x] != 0: #west
                filled = 1
            elif ori == 1 and board[row][col+x] != 0: #east
                filled = 1
            elif ori == 2 and board[row+x][col] != 0: #south
                filled = 1

        #Fill squares. Increase parameter.
        if filled == 0:
            for x in range(size):
                if ori == -2: #north
                    board[row-x][col] = '|'
                elif ori == -1: #west
                    board[row][col-x] = '-'
                elif ori == 1: #east
                    board[row][col+x] = '-'
                else: #south
                    board[row+x][col] = '|'
            size += 1
    return board


def attack(opp_board, hidden):
    LET_NUM = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    NUMBERS = "12345678"

    while True:
        #Get coordinates from user. Validate input. If valid, update board.
        print("\nType the coordinates you would like to fire at.")
        coor = input("\t(Format: letter number) ").lower().strip().split()
        if coor[0] in LET_NUM and coor[1] in NUMBERS:
            col = LET_NUM[coor[0]]
            row = int(coor[1])-1
            
            if opp_board[row][col] == " " or opp_board[row][col] == ".":
                color.write("\tYou've already hit that spot.\n", "KEYWORD")
            else:
                opp_board = update_board(opp_board, row, col, hidden)
                break
        else:
            color.write("\tCoordinates are invalid. Please try again.\n", "KEYWORD")
    return opp_board


def cpu_attack(board):
    #Generate a random spot to attack. Check that it hasn't already been hit.
    #   Update board.
    while True:
        row = random.randint(0, 7)
        col = random.randint(0, 7)

        if board[row][col] != " " and board[row][col] != ".":
            board = update_board(board, row, col)
            break
    return board


def print_board(board, owner):
    #Loop through the board. Print it.
    #   Fonts make the output of this kinda weird.
    #   Recommend bolded Courier
    print("\n\n%s Board:\n" % owner)
    print('{:^60s}'.format("  A B C D E F G H"))

    for row in range(len(board)):
        #Construct string to be printed mid-screen
        s = str(row + 1)
        for square in board[row]:
            s += " " + str(square)

        print('{:^60s}'.format(s))
    print()


def update_board(board, row, col, hidden=[]):
    LETTERS = "ABCDEFGH"

    #Determine if this was a user attack or a computer attack
    if len(hidden) > 0:

        #User attack - check to see if the computer has a ship in that spot.
        #   Computer ships are listed in hidden board, not the displayed
        #   board.
        if hidden[row][col] in ["-", "|"]:
            board[row][col] = "."
            color.write("\tHit!\n", "STRING")
        else:
            board[row][col] = " "
            color.write("\tMiss.\n", "COMMENT")    
    else:
        #Computer attack - check to see if user has a ship in that spot.
        print("Computer shoots at %s %d..." % (LETTERS[col], row+1))
        if board[row][col] in ["-", '|']:
            board[row][col] = "."
            color.write("\tHit!\n", "STRING")
        else:
            board[row][col] = " "
            color.write("\tMiss.\n", "COMMENT")
    return board


def check_win(board, hidden=[]):
    if len(hidden) > 0:
        for row in range(len(hidden)):
            for col in range(len(board[row])):
                if hidden[row][col] in ['-', '|'] and board[row][col] == 0:
                    #If any ship has not been hit, in other words
                    return 0
    else:
        for row in board:
            for square in row:
                if square in ['-', '|']: #If any ship hasn't been hit
                    return 0
    return 1


def rules():
    print("\nYou and the computer each get 3 ships:")
    print("\ta battleship  (fills 4 squares)")
    print("\ta destroyer   (fills 3 sqaures)")
    print("\ta patrol boat (fills 2 squares)")

    print("\nThe goal is to sink all your opponent's ships before they can sink yours!")
    print("First you'll set up your ships. You can manually place them or have their\nlocations randomly generated.")

    print("\nEach round, you'll be asked to enter coordinates for a firing spot.")
    print("Depending on what you hit, a message will pop up.")

    print("\nThe boards will also update with each turn. Here's the key:")
    print("\t\"0\" - an unattacked space")
    print("\t\" \" - an attacked empty space")
    print("\t\".\" - an attacked filled space - a hit ship")
    print("\t\"-\" - your ship, going horizontally across the board")
    print("\t\"|\" - your ship, going vertically across the board")

    print("\nIf your board doesn't line up right, try changing IDLE's font.")
    print("Courier (bolded) is recommended.")

    input("\nPress enter to continue...")
    main_menu()

main_menu()
