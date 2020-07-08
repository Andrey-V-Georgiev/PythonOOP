from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        add_list = list(args)
        sum_args = reduce((lambda x, y: x + y), add_list)
        return sum_args

    @staticmethod
    def multiply(*args):
        multiply_list = list(args)
        multiply_args = reduce((lambda x, y: x * y), multiply_list)
        return multiply_args

    @staticmethod
    def divide(*args):
        divide_list = list(args)
        divide_args = reduce((lambda x, y: x / y), divide_list)
        return divide_args

    @staticmethod
    def subtract(*args):
        subtract_list = list(args)
        subtract_args = reduce((lambda x, y: x - y), subtract_list)
        return subtract_args


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

