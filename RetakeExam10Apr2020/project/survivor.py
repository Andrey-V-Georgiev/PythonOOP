class Survivor:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = 100
        self.needs = 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '':
            raise ValueError('Name not valid!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 0:
            raise ValueError('Age not valid!')
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):
        if value < 0:
            raise ValueError('Health not valid!')
        self.__health = value if value < 100 else 100

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value: int):
        if value < 0:
            raise ValueError('Needs not valid!')
        self.__needs = value if value < 100 else 100

    @property
    def needs_sustenance(self):
        return True if self.needs < 100 else False

    @property
    def needs_healing(self):
        return True if self.health < 100 else False
