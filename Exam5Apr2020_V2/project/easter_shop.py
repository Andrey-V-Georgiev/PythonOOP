from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self,
                 name: str,
                 chocolate_factory: ChocolateFactory,
                 egg_factory: EggFactory,
                 paint_factory: PaintFactory):

        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()  # 1D

    def add_chocolate_ingredient(self, ingredient_type: str, quantity: int):
        self.chocolate_factory.add_ingredient(ingredient_type, quantity)

    def add_egg_ingredient(self, ingredient_type: str, quantity: int):
        self.egg_factory.add_ingredient(ingredient_type, quantity)

    def add_paint_ingredient(self, ingredient_type: str, quantity: int):
        self.paint_factory.add_ingredient(ingredient_type, quantity)

    def make_chocolate(self, recipe_name: str):
        self.chocolate_factory.make_chocolate(recipe_name)
        if recipe_name in self.storage.keys():
            self.storage[recipe_name] += 1
        else:
            self.storage[recipe_name] = 1

    def paint_egg(self, color: str, egg_type: str):
        have_color = False
        if color in self.paint_factory.ingredients.keys():
            if self.paint_factory.ingredients[color] > 0:
                have_color = True

        have_eggs = False
        if egg_type in self.egg_factory.ingredients.keys():
            if self.egg_factory.ingredients[egg_type] > 0:
                have_eggs = True

        if have_color and have_eggs:
            self.paint_factory.remove_ingredient(color, 1)
            self.egg_factory.remove_ingredient(egg_type, 1)
            egg_name = f"{color} {egg_type}"
            if egg_name in self.storage.keys():
                self.storage[egg_name] += 1
            else:
                self.storage[egg_name] = 1
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        result = f"Shop name: {self.name}\n"
        result += f"Shop Storage:\n"
        for name, quantity in self.storage.items():
            result += f"{name}: {quantity}\n"
        return result

