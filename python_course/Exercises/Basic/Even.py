#define the list that will contain even numbers
even =[]

#check if the number is even
while len(even)<6:
    #ask user for number to insert
    num = int(input("Enter a positive number: "))
    
    if num%2 == 0:
        print("the number is even")
        even.append(num)
    else:
        print("the number is odd")
    
print("5 even numbers found")