from abc import ABC, abstractmethod


class Factory(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = dict()  # 1D

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        self.__capacity = value

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, quantity: int):
        possible = True if len(self.ingredients) + quantity <= self.capacity else False
        return possible
