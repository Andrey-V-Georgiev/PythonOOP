class vowels:
    def __init__(self, string):
        self.string = list(string)
        self.start = 0
        self.end = len(self.string) - 1
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            i = self.string[self.start]
            self.start += 1
            if i in self.vowels:
                return i
            else:
                return self.__next__()
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
