class Rhombus:
    def __init__(self, _size):
        self.size = _size

    def print(self):
        # print upper part
        for i in range(1, self.size + 1):
            [print(' ', end='') for _ in range(self.size - i)]
            [print('* ', end='') for _ in range(i)]
            print()
        # print down part
        for j in range(self.size - 1, 0, -1):
            [print(' ', end='') for _ in range(self.size - j)]
            [print('* ', end='') for _ in range(j)]
            print()


size = int(input())
r = Rhombus(size)
r.print()
