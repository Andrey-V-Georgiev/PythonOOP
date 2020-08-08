from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = list()  # survivor objects
        self.supplies = list()  # supply objects
        self.medicine = list()  # medicine objects

    @property
    def food(self):
        food_supplies = [s for s in self.supplies if s.__class__.__name__ == 'FoodSupply']
        if len(food_supplies) == 0:
            raise IndexError('There are no food supplies left!')
        return food_supplies

    @property
    def water(self):
        water_supplies = [s for s in self.supplies if s.__class__.__name__ == 'WaterSupply']
        if len(water_supplies) == 0:
            raise IndexError('There are no water supplies left!')
        return water_supplies

    @property
    def painkillers(self):
        painkiller_medicines = [m for m in self.medicine if m.__class__.__name__ == 'Painkiller']
        if len(painkiller_medicines) == 0:
            raise IndexError('There are no painkillers left!')
        return painkiller_medicines

    @property
    def salves(self):
        salves_medicines = [m for m in self.medicine if m.__class__.__name__ == 'Salve']
        if len(salves_medicines) == 0:
            raise IndexError('There are no salves left!')
        return salves_medicines

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            pill = self.painkillers.pop() if medicine_type == 'Painkiller' else self.salves.pop()
            survivor.health += pill.health_increase
            self.medicine.remove(pill)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            supply = self.food.pop() if sustenance_type == 'FoodSupply' else self.water.pop()
            survivor.needs += supply.needs_increase
            self.supplies.remove(supply)
            return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for s in self.survivors:
            reduce_value = s.age * 2
            s.needs -= reduce_value

        for s in self.survivors:
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')
