# Importing Dependencies #
from Game import TicTacToe
from User import USER


# Creating Users #
Vinit = USER(username='Vinit', userSymbol='X')
Yashwant = USER(username='Yashwant', userSymbol='O')

# Creating Game Object #
game = TicTacToe(user1=Vinit, user2=Yashwant)


# Playing Game #
while not game.isGameEnded():
    print(f"Chance of {game.gameBoard.userToMakeMove.username}.")
    row = int(input("Enter Row: "))
    col = int(input("Enter Row: "))
    game.makeMove(row, col)


# Displaying Game Result #
print(game.getGameResult())

# Displaying Game Highlight / Summary #
if input("Do you want to see the highlights of the game(y/n): ").lower() == 'y':
    print(game.getGameHighlights())