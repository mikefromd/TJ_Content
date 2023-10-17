# Rock, Paper, Scissor Game, with Command Line

from random import randint

  
player = input('rock (r), paper (p) or scissors (s)?')

# Pictogram for rock o
if(player == 'r'):
  print('O', end=' ')
  
# Pictogram for paper ___  
elif(player == 'p'):
  print('___', end=' ')

# Pictogram for scissors >8  
elif(player == 's'):
  print('>8', end=' ')

# Wrong data entry
else:
  print('??')
  
print('vs', end=' ')

# The computer makes its choice
chosen = randint(1,3)

# Print the choice of the computer
if(chosen == 1):
  computer = 'r'
  print('O')
  
elif(chosen == 2):
  computer = 'p'
  print('___')
  
else:
  computer = 's'
  print('>8')

# Calculate who has won the game
if(player == computer):
  print('DRAW!')
  
elif(player == 'r' and computer == 's'):
  print('Player wins!')
  
elif(player == 'r' and computer == 'p'):
  print('Computer wins!')
  
elif(player == 'p' and computer == 'r'):
  print('Player wins!')
  
elif(player == 'p' and computer == 's'):
  print('Computer wins!')

elif(player == 's' and computer == 'p'):
  print('Player wins!')
  
elif(player == "s" and computer == 'r'):
  print('Computer wins!')

else:
  print('Huh?')
  
  