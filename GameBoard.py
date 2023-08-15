# Class GameBoard #
class GameBoard:
    ROWS = 3
    COLUMNS = 3
    # Initializing GameBoard #
    def __init__(self, user1, user2):
        self.board = [[None for _ in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.user1 = user1
        self.user2 = user2
        self.userToMakeMove = self.user1
        self.winner = None
        self.isGameDraw = False


    # Decorator/Middleware to find the given position represents a valid cell or not #
    def validCell(method):
        def decorate(*args, **kwargs):
            row = args[1]
            col = args[2]
            if row < 0 or row >= GameBoard.ROWS or col < 0 or col >= GameBoard.COLUMNS:
                print("Invalid move position.")
                return False
            else:
                return method(*args, **kwargs)
        return decorate


    # Decorator/Middleware to find the move is a valid move or not #
    def validMove(method):
        def decorate(*args, **kwargs):
            row = args[1]
            col = args[2]
            if args[0].board[row][col] is not None:
                print(f"Position is already filled with move {args[0].board[row][col]}.")
                return False
            else:
                return method(*args, **kwargs)
        return decorate


    # Decorator/Middleware to find whether the game is ended or not #
    def gameIsOn(method):
        def decorate(*args, **kwargs):
            if args[0].winner is not None:
                print(f"Game has ended, Winner : {args[0].winner.username}.")
                return False
            elif args[0].isGameDraw is not False:
                print("Game has ended with Draw.")
                return False
            else:
                return method(*args, **kwargs)
        return decorate


    # Method to make a user move on the specified position in the board #
    @validCell
    @validMove
    @gameIsOn
    def makeMove(self, row, col):
        self.board[row][col] = self.userToMakeMove.userSymbol
        if self.isWinningMove(row, col):
            self.winner = self.userToMakeMove
        elif self.isGameEndedWithDraw():
            self.isGameDraw = False
        moveMadeBy = self.userToMakeMove
        self.switchUserToMakeMove()
        return moveMadeBy


    # Method to find whether the current move has ended the game or not #
    def isWinningMove(self, row, col):
        horizontal = True
        vertical = True
        diagonal = True
        reverseDiagonal = True
        for i in range(self.ROWS):
            if self.board[i][col] != self.userToMakeMove.userSymbol:
                vertical = False
            if self.board[row][i] != self.userToMakeMove.userSymbol:
                horizontal = False
            if self.board[i][i] != self.userToMakeMove.userSymbol:
                diagonal = False
            if self.board[i][self.COLUMNS-i-1] != self.userToMakeMove.userSymbol:
                reverseDiagonal = False
        return horizontal or vertical or diagonal or reverseDiagonal


    # Method to find the whether the game is draw or not #
    def isGameEndedWithDraw(self):
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                if self.board[row][col] is None:
                    return False
        return True


    # Method to switch between both the users #
    def switchUserToMakeMove(self):
        self.userToMakeMove = self.user1 if self.userToMakeMove == self.user2 else self.user2