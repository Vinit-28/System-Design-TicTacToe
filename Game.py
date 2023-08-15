# Importing the Dependencies #
import uuid
from GameBoard import GameBoard


# TicTacToe Game Class #
class TicTacToe:
    # Initializing the Game #
    def __init__(self, user1, user2):
        self.gameId = uuid.uuid4()
        self.gameBoard = GameBoard(user1, user2)
        self.user1 = user1
        self.user2 = user2
        self.winner = None
        self.loser = None
        self.movesHistory = list()


    # Method to make a move in the game #
    def makeMove(self, row, col):
        moveMadeBy = self.gameBoard.makeMove(row, col)
        if moveMadeBy:
            if self.gameBoard.winner is not None:
                print(f"Game has ended. Winner : {self.gameBoard.winner.username}")
                self.setWinner()
                self.setLoser()
                self.winner.updateUserStats(gameId=self.gameId, result='Won', opponent=self.loser)
                self.loser.updateUserStats(gameId=self.gameId, result='Loose', opponent=self.winner)
            elif self.gameBoard.isGameDraw:
                print("Game has ended with Draw.")
                self.user1.updateUserStats(gameId=self.gameId, result='Draw', opponent=self.user2)
                self.user2.updateUserStats(gameId=self.gameId, result='Draw', opponent=self.user1)
            self.storeMove(moveMadeBy, row, col)


    # Method to set winner of the game #
    def setWinner(self):
        self.winner = self.user1 if self.gameBoard.winner == self.user1 else self.user2


    # Method to set loser of the game #
    def setLoser(self):
        self.loser = self.user2 if self.gameBoard.winner == self.user1 else self.user1


    # Method to store the user move #
    def storeMove(self, moveMadeBy, row, col):
        self.movesHistory.append({
            'Move Number': len(self.movesHistory)+1,
            'User': moveMadeBy,
            'Position': [row, col],
            'Symbol': moveMadeBy.userSymbol
        })


    # Method to find whether the game has ended or not #
    def isGameEnded(self):
        return self.winner is not None and self.loser is not None


    # Method to get the result of the game #
    def getGameResult(self):
        return f'''Game Statistics:
            Winner: {self.winner},
            Loser: {self.loser}
        '''


    # Method to get the game's highlight / summary #
    def getGameHighlights(self):
        tableHeaders = 'Move Number\tUser\tPosition\tSymbol\n'
        tableData = ''
        for move in self.movesHistory:
            tableRow = f'{move.get("Move Number")}\t{move.get("User").username}\t{move.get("Position")}\t{move.get("Symbol")}\n'
            tableData += tableRow
        return tableHeaders + tableData