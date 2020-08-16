from project.factory.factory import Factory

allowed_types = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]


class ChocolateFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = dict()  # 2D
        self.products = dict()  # 1D

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in allowed_types:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type in self.ingredients.keys():
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")

        recipe_ingredients = self.recipes[recipe_name]

        have_ingredients = True
        for recipe_ingredient_name, recipe_ingredient_quantity_1 in recipe_ingredients.items():
            if self.ingredients[recipe_ingredient_name] < recipe_ingredient_quantity_1:
                have_ingredients = False

        if have_ingredients:
            for recipe_ingredient_type, recipe_ingredient_quantity_2 in recipe_ingredients.items():
                self.remove_ingredient(recipe_ingredient_type, recipe_ingredient_quantity_2)

            if recipe_name in self.products.keys():
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1



