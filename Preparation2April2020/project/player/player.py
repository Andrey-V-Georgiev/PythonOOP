from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    @abstractmethod
    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name: str):
        if name == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points

    @property
    def is_dead(self):
        return self.health <= 0

