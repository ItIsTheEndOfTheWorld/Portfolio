#Kylee Willis
import random

#Program that simulates a rock-paper-scissors-lizard-spock game.

user_data = ["", 0, 0, 0] #user name, wins, losses, ties

def menu():
    #Create the first landing menu. Handle user choices appropriately.
    while True:
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            start_game()
            break
        elif choice == "2":
            load_game()
            break
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("That is an invalid choice; please type \"1\", \"2\", or \"3\".\n")
    return 0


def start_game():
    #Really just used to get user's name
    global user_data
    name = input("\nWhat is your name? ").strip()
    user_data[0] = name
    
    print("Hello %s. Let's play!" % name)
    gameplay()


def load_game():
    #Load the user's game, if it exists.
    global user_data
    name = input("\nWhat is your name? ").strip()
    
    try:
        file = open("%s.rps" % name, "r") #Could cause error, handled by except
        print("Welcome back %s. Let's play!\n" % name)

        #Read each line. Format of line 1: "name|wins|losses|ties"
        line = file.readline().split("|")
        for x in range(len(line)):
            try:
                user_data[x] = int(line[x])
            except:
                user_data[x] = line[x]

        #Add wins, losses, and ties to get the total number of games played
        game = user_data[1] + user_data[2] + user_data[3]
        file.close()
        
        gameplay(game)
    
    except FileNotFoundError:
        print("%s, your game could not be found.\n" % name)
        menu()


def gameplay(game=1):
    user_move = -1
    win_lose = ""
    moves = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    #Set up the gameplay menu. Allow the user to pick a move.
    while True:
        print("\n\nRound %d\n" % game)

        for i in range(len(moves)):
            print("%d. %s" % (i+1, moves[i]))

        user = input("\nWhat will it be? ").strip()
        if user not in ["1", "2", "3", "4", "5"]:
            print("Please select a valid move; type \"1\", \"2\", \"3\", \"4\", or \"5\".")
        else:
            user_move = int(user)
            break
    
    cpu_move = random.choice(moves)


    #Determine if user won, lost or tied with the cpu
    if user_move == 1: #user chose rock
        win_lose = win_lose_tie(["Lizard, Scissors"], ["Paper", "Spock"], cpu_move)
    elif user_move == 2: #user chose paper
        win_lose = win_lose_tie(["Rock", "Spock"], ["Scissors", "Lizard"], cpu_move)
    elif user_move == 3: #user chose scissors
         win_lose = win_lose_tie(["Paper", "Lizard"], ["Rock", "Spock"], cpu_move)
    elif user_move == 4: #user chose lizard
        win_lose = win_lose_tie(["Paper", "Spock"], ["Rock", "Scissors"], cpu_move)
    else:                         #user chose spock
        win_lose = win_lose_tie(["Rock", "Scissors"], ["Paper", "Lizard"], cpu_move)
    
    print("\nYou chose %s. The computer chose %s. You %s!\n" % (user_move, cpu_move, win_lose))

    
    #Set up the second landing menu 
    while True:
        print("What would you like to do?\n")

        print("1. Play Again")
        print("2. View Statistics")
        print("3. Quit")

        choice = input("\nEnter choice: ")
        
        if choice == "1":
            gameplay(game+1)
            return
        elif choice == "2":
            statistics()
        elif choice == "3":
            #Save the user's game
            try:
                file = open("%s.rps" % user_data[0], "w")

                #format: "name|wins|losses|ties"
                file.write(user_data[0] + "|" + str(user_data[1]) + "|" + str(user_data[2]) + "|" + str(user_data[3]))
                file.close()
                print("%s, your game has been saved." % user_data[0])

            except Exception as e:
                print("Sorry %s, the game could not be saved." % user_data[0])
                print(e)
            return
        else:
            print("Please enter a valid choice; type \"1\", \"2\", or \"3\".\n")


def win_lose_tie(win, lose, cpu_move):
    #Determines if the user won, lost, or tied based on lists sent in
    global user_data
    
    if cpu_move in win:
        user_data[1] = user_data[1] + 1
        return "win"
    
    elif cpu_move in lose:
        user_data[2] = user_data[2] + 1
        return "lose"
    
    user_data[3] = user_data[3] + 1
    return "tie"


def statistics():
    #Print statistics
    print("\n%s, here are your game play statistics..." % user_data[0])
    print("Wins: %d" % user_data[1])
    print("Losses: %d" % user_data[2])
    print("Ties: %d" % user_data[3])

    print("Win/Loss Ratio: %.2f\n" % (user_data[1]/user_data[2]))


def main():
    print("Welcome to Rock, Paper, Scissors!\n")
    menu()
main()
