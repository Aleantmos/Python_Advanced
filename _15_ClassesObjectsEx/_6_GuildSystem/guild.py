from player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if self.players.__contains__(player):
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {self.name} has been removed from the guild."

        return f"Player {self.name} is not in the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"

        for player in self.players:
            res += player.player_info() + "\n"

        return res
