from project.factory.factory import Factory

allowed_chocolate_ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]


class ChocolateFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = dict()  # recipe name as key and dictionary of needed ingredients to make the recipe
        self.products = dict()  # made recipes; recipe name as key and quantity as value

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in allowed_chocolate_ingredients:
            raise TypeError(f'Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}')
        if not self.can_add(quantity):
            raise ValueError('Not enough space in factory')
        if ingredient_type in self.ingredients.keys():
            self.ingredients[ingredient_type] += quantity
        else:
            self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError('No such product in the factory')
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError('Ingredient quantity cannot be less than zero')
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes.keys():
            raise TypeError('No such recipe')

        recipe = self.recipes[recipe_name]

        # check for ingredients availability
        have_all_ingredients = True
        for ingredient_name, quantity in recipe.items():
            if self.ingredients[ingredient_name] < quantity:
                have_all_ingredients = False
        if have_all_ingredients:
            # remove used ingredients
            for ingredient_name, quantity in recipe.items():
                self.remove_ingredient(ingredient_name, quantity)

            # add to products or increase
            if recipe_name in self.products.keys():
                self.products[recipe_name] += 1
            else:
                self.products[recipe_name] = 1
