from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in ["white", "yellow", "blue", "green", "red"]:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}')
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')
        if ingredient_type in self.ingredients.keys():
            self.ingredients[f'{ingredient_type}'] += quantity
        else:
            self.ingredients[f'{ingredient_type}'] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError('No such ingredient in the factory')
        if self.ingredients[f'{ingredient_type}'] < quantity:
            raise ValueError('Ingredient quantity cannot be less than zero')
        self.ingredients[f'{ingredient_type}'] -= quantity

    @property
    def products(self):
        return self.ingredients
