# List data
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, 2, "Bob", False]

# Access list elements using an index starting from 0
print(numbers[0])
print(names[1])
print(mixed[3])

# an element can be modified via the index
numbers[2] = 20
print(numbers)

# some methods are:
# len for length 
print(len(numbers))
# append to add an element to the end of the list
numbers.append(6)
print(numbers)
# insert to insert an element at a specific position
numbers.insert(1, 10)
print(numbers)
# remove to remove an element
numbers.remove(4)
print(numbers)
# sort to organize the list
numbers.sort()
print(numbers)
# pop removes the last element of a list
numbers.pop()
print(numbers)