class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(iterable) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            i = self.iterable[self.start]
            self.start -= 1
            return i
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

