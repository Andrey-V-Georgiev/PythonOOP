class Stack:
    def __init__(self):
        self.data = list()

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        rev_data = self.data[::-1]
        rev_data_str = ', '.join(rev_data)
        return f'[{rev_data_str}]'


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))  # '[carrot, apple]'
print(stack.pop())  # 'carrot'
print(stack.peek())  # 'apple'
stack.push("cucumber")
print(str(stack))  # '[cucumber, apple]'
print(stack.is_empty())  # False
