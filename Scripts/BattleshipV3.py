# Battle Ship

# Further improvements:
# - Replace guess_row and guess_col with x, y to reduce typing of the code.
#
#

from random import randint

tries = 5    # How many times the player can guess
size = 5     # Size of the game board
def print_board(board):
    for row in board:
        print(' ' + str(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

def shoot(ship_row, ship_col):
    turn = 1 # counter for turns played
    while turn <= tries:   # Loop through the five turns
        print()
        print("It's turn " + str(turn))
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Column: "))
        print("Your guess: ", guess_row, guess_col)
    
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk the ship")
            board[ship_row][ship_col] = "#"
            print_board(board)
            break
        else:
            if (guess_row < 0 or guess_row > size-1) or \
            (guess_col < 0 or guess_col > size-1):
                print("Oops, that's outside the game board!")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that position already!")
            else:
                print("You missed the ship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            turn += 1


# Main Program

# Initialize empty game board
board = []
repeat size:
    board.append(["0"] * size)
                     
# Welcome and game rules, print game board at start                                                           
print("Let's play BATTLESHIP")
print("You have ", tries, " tries to find a 1x1 boat on the playing field.")
print("The row numbers and column numbers are from 0 to ", size-1, " the field has a size of ", size, " x ", size)
print("0 -> not shot, X -> shot, # -> location of ship")
print("Good luck!")
print_board(board)

# Choose location of the ship
ship_row = random_row(board)
ship_col = random_col(board)

# Main loop
shoot(ship_row, ship_col)

print()          
print("Game Over")
print("Here is the solution:")
board[ship_row][ship_col] = "#"
print_board(board)
            