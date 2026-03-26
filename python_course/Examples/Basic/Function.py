# greet function definition
def greet(name):
    print("Hello,", name)
    print("Welcome to our program")

# sum function definition
def sum_nums(a, b):
    result = a + b
    print("The sum is:", result)
    
# execute the declared functions 
greet("Alice")
sum_nums(3, 4)

# function with return
def square(num):
    return num * num

# store the result returned by the function in a variable
result = square(2)
print("The square is:", result)