numbers = [1, 2, 3, 4, 5]

# break terminates the loop
# continue skips the iteration, but then continues with the next one
for number in numbers:
    if number == 2:
        continue
    elif number == 4:
        break
    else:
        print(number)
    
print("\nResults of pass:")
# pass does not perform any action
for i in range(5):
    if i == 3:
        pass
    print(i)

print("\nResults of splat operator:")    
# splat: * before the iterable variable to expand it 
numbers = [*range(1, 11)]
print(numbers)