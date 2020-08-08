from project.supply.supply import Supply


class FoodSupply(Supply):
    def __init__(self):
        # super().__init__(20)
        Supply.__init__(self, 20)


