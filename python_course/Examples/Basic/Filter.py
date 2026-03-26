# define the function for the filter
def is_even(x):
    return x%2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# use the filter function by applying the function to the iterable element
even_numbers = list(filter(is_even, numbers))
print(even_numbers)