from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str,
                 chocolate_factory: ChocolateFactory,
                 egg_factory: EggFactory,
                 paint_factory: PaintFactory
                 ):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe_name: str):
        self.chocolate_factory.make_chocolate(recipe_name)
        if recipe_name in self.storage:
            self.storage[recipe_name] += 1
        else:
            self.storage[recipe_name] = 1

    def paint_egg(self, color: str, egg_type: str):
        egg_ingredients = self.egg_factory.products
        have_eggs = False
        if egg_type in egg_ingredients.keys():
            egg_ingredient_quantity = egg_ingredients[egg_type]
            if egg_ingredient_quantity > 0:
                have_eggs = True

        paint_ingredients = self.paint_factory.products
        have_color = False
        if color in paint_ingredients.keys():
            paint_ingredients_quantity = paint_ingredients[color]
            if paint_ingredients_quantity > 0:
                have_color = True

        if have_eggs and have_color:
            storage_key = f'{color} {egg_type}'
            if storage_key in self.storage:
                self.storage[f'{storage_key}'] += 1
            else:
                self.storage[f'{storage_key}'] = 1
            self.egg_factory.remove_ingredient(egg_type, 1)
            self.paint_factory.remove_ingredient(color, 1)
        else:
            raise ValueError('Invalid commands')

    def __repr__(self):
        str_result = f'Shop name: {self.name}\n'
        str_result += f'Shop Storage:\n'
        for name, quantity in self.storage.items():
            str_result += f'{name}: {quantity}\n'
        return str_result
