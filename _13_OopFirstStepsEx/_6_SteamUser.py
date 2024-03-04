class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if self.games.__contains__(game):
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        return f"{game} is not in library"

    def buy_game(self, game):
        if self.games.__contains__(game):
            return f"{game} is already in yout library"

        self.games.append(game)
        return f"{self.username} bought {game}"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
