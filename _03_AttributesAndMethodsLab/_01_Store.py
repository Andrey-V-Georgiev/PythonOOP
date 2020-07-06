class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item_name):
        if len(self.items) + 1 > self.capacity:
            return f'Not enough capacity in the store'
        else:
            if item_name in self.items.keys():
                self.items[item_name] += 1
            else:
                self.items[item_name] = 1
            self.capacity -= 1
            return f'{item_name} added to the store'

    def remove_item(self, item_name, amount):
        if item_name not in self.items.keys():
            return f'Cannot remove {amount} {item_name}'
        else:
            if self.items[item_name] < amount:
                return f'Cannot remove {amount} {item_name}'
            else:
                self.items[item_name] -= amount
                return f'{amount} {item_name} removed from the store'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)
print(first_store)
print(second_store)
print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
