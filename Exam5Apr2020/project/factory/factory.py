from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = dict()

    @property
    def name(self):
        pass

    @name.setter
    def name(self, value: str):
        pass

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        pass

























































































