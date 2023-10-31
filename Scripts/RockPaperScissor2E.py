# Rock, Paper, Scissor Game, with Command Line
# Pictrograms are rock -> 'o', paper -> '___', and scissors -> '>8'
# Integer coding for winner -> player 1, computer 2, Draw 0

from random import randint

def getPlayerInput():
    player = input('rock (r), paper (p) or scissors (s)?')
    if(player == 'r'):
        print('O', end=' ')
    elif(player == 'p'):
        print('___', end=' ')
    elif(player == 's'):
        print('>8', end=' ')
    else:
        print('??') # input not recognized
    return player    


def getComputerInput():
    chosen = randint(1,3)
    if(chosen == 1):
        computer = 'r'
        print('O')
  
    elif(chosen == 2):
        computer = 'p'
        print('___')
  
    else:
        computer = 's'
        print('>8')
    return computer


def calcWinner(player, computer):
    if(player == 'r' and computer == 's'):
        print('Player wins!')
        return 1
  
    elif(player == 'r' and computer == 'p'):
        print('Computer wins!')
        return 2
  
    elif(player == 'p' and computer == 'r'):
        print('Player wins!')
        return 1
  
    elif(player == 'p' and computer == 's'):
        print('Computer wins!')
        return 2

    elif(player == 's' and computer == 'p'):
        print('Player wins!')
        return 1
  
    elif(player == "s" and computer == 'r'):
        print('Computer wins!')

    else:
        print('Huh?')

      
# Main Program.  
player = getPlayerInput()                        
print('vs', end=' ')
computer = getComputerInput()
result = calcWinner(player, computer)
print("The game result: ", result)


  
  