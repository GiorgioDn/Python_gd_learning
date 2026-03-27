# Import all functions from the Fibonacci.py file
from .Import.Fibonacci import *
        
while True:
    # Ask for the sequence number
    num_fibonacci = int(input("Type a positive integer for the Fibonacci sequence: "))
    # Initialize the list with results
    list_res = []
    # Result of the sequence version
    result = fibonacci_succ(num_fibonacci, list_res)
    print(result)
    
    # Recursive result with only the result returned for num_fibonacci
    result_ric = fibonacci_recursive(num_fibonacci)
    print(result_ric)
    
    choice = input("Do you want to continue entering numbers? ")
    
    if choice.lower() == "no":
        break
