count = 0

# initialize a while loop that runs until the condition is met
# mathematical loop
while count < 5:
    print(count)
    count += 1
    
controller = True

# boolean loop
while controller:
    print(controller)
    choice = input("Do you want to continue? ")
    if choice.lower() == "no":
        controller = False
    else:
        print("You are continuing")
        
numbers = [1, 2, 3, 4, 5]

# for loop 
for number in numbers:
    print(number)
    
# add a newline to better distinguish the for loops
print("\n")
    
# for loop with range (stop only)
for i in range(5):
    print(i)

print("\n")

# for loop with range (start and stop)
for i in range(2, 8):
    print(i)

print("\n")

# for loop with range (start, stop, and step)
for i in range(2, 10, 2):
    print(i)

print("\n")