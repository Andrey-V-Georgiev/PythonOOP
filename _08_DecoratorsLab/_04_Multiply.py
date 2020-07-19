def multiply(times):
    def decorator(function):
        def wrapper(number):
            func_result = function(number)
            decorator_result = func_result * times
            return decorator_result
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
