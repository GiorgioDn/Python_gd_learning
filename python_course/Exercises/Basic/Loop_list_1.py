#Initialize the list
list_num = []

#let the user select 5 numbers to add to the list
while len(list_num)<6:
    list_num.append(float(input("Type a number: ")))

#print the square of each number in the list
for n in list_num:
    n = n**2
    print(n)