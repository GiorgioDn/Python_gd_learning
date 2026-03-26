# decorator declaration
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# initialize the decorator
@decorator
def greet():
    print("Hello")

# launch the greet function modified by the wrapper
greet()

print()

# decorator with arguments
def decorator_with_arguments(func):
    def wrapper(*args, **kwargs):
        print ("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator_with_arguments
def sum_nums(a, b):
    print(a + b)
    return a + b

# use the same wrapper for a function with more parameters
@decorator_with_arguments
def multipleSum(a, b, c, d):
    print(a + b + c + d)
    return a + b + c + d

print("The result is:", sum_nums(4, 5))

print("The result is:", multipleSum(1, 2, 4, 3))

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Call to {func.__name__} with arguments: {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result of {func.__name__}: {result}")
        return result
    return wrapper

@logger
def multiply (a, b):
    return a*b

multiply (3, 5)