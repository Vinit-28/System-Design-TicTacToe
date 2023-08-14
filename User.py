class USER:
    def __init__(self, username, userSymbol):
        self.username = username
        self.userSymbol = userSymbol
        self.games_played = dict()
        self.games_won = 0

    def updateUserStats(self, gameId, result, opponent):
        self.games_won += 1 if result.lower() == 'won' else 0
        self.games_played[gameId] = {
            "GameId": gameId,
            "Result": result,
            "Opponent": opponent
        }

    def __repr__(self):
        return f"{self.username}({self.userSymbol})"
