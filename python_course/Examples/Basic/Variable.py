# integer variable types
x = 1
y = -5

print(x, y)

# float variable types (uses . and not ,)
x = 3.14
y = -5.46

print(x, y)

# string variable types
x = "blackberry"
y = "meters"

print(x, y)

# string char index 
print("Char b of string x: ", x[0])
print("Char e of string y: ", y[1])

# string concatenation
conc = x + " 3.3 " + y 

print(conc)

# string methods
# len = string length
print(len(x))

# upper = converts string to uppercase
print(x.upper())

# lower = converts string to lowercase
print(x.lower())

# split = splits into a list of substrings
print(conc.split())

# also based on a delimiter
concDel = conc + ", " + x
print(concDel.split(','))

# replace = replaces part of a string with another
print(conc.replace('blackberry', 'distance'))

# char type
char = "A"
print(char)

# boolean variable types True or False
x = True
y = False 

print(x, y)

# Boolean values True or False can be used with logical operators 
x = 5
y = 10
z = 7

# and returns true if both conditions are true
print("The boolean value of: x < y and z < y is:", x < y and z < y)

# or returns true if at least one of the conditions is true
print("The boolean value of: x < y or x > z is:", x < y or x > z)

# not returns the opposite boolean value
print("The boolean value of: not(x < y) is:", not(x < y))

# comparison operators, return a boolean value
# == equal to
print("The boolean value of: x == y is:", x == y)

# != different from 
print("The boolean value of: x != y is:", x != y)

# < less than 
print("The boolean value of: x < y is:", x < y)

# > greater than 
print("The boolean value of: x > y is:", x > y)

# <= less than or equal to 
print("The boolean value of: x <= y is:", x <= y)

# >= greater than or equal to
print("The boolean value of: x >= y is:", x >= y)