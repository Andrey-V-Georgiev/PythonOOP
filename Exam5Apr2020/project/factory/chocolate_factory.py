from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = dict()
        self.products = dict()

    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def add_recipe(self, recipe_name: str, recipe: dict):
        pass

    def make_chocolate(self, recipe_name: str):
        pass
