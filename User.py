# Class USER #
class USER:
    # Method to initialize the user object #
    def __init__(self, username, userSymbol):
        self.username = username
        self.userSymbol = userSymbol
        self.games_played = dict()
        self.games_won = 0
        self.games_lost = 0
        self.games_tied = 0


    # Method to update the User Statistics #
    def updateUserStats(self, gameId, result, opponent):
        if result.lower() == 'won':
            self.games_won += 1
        elif result.lower() == 'loose':
            self.games_lost += 1
        else:
            self.games_tied += 1
        self.games_played[gameId] = {
            "GameId": gameId,
            "Result": result,
            "Opponent": opponent
        }


    # User object representation #
    def __repr__(self):
        return f"{self.username}({self.userSymbol})"