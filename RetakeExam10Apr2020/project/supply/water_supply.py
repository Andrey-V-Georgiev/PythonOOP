from project.supply.supply import Supply


class WaterSupply(Supply):
    def __init__(self):
        # super().__init__(40)
        Supply.__init__(self, 40)
