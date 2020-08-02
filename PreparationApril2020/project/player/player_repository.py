from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.players = list()

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        player = self.find(player_name)
        self.players.remove(player)

    def find(self, username: str):
        player = [player for player in self.players if player.username == username][0]
        return player
