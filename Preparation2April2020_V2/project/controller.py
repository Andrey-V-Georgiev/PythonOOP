from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        player = Beginner(username) if type == "Beginner" else Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        card = MagicCard(name) if type == "Magic" else TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {p.card_repository.count}\n"
            for c in p.card_repository.cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result
