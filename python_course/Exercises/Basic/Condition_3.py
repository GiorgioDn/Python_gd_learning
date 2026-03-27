#selection of two int numbers from user
print ("Select two numbers")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

#I write available operations and let user choose
print("Select the corresponding operation number: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
operation = int(input())

#associate corresponding operation based on user input
match operation:
    case 1: 
        operation = num1 + num2
        print("Addition returned: ", operation)
    case 2: 
        operation = num1 - num2
        print("Subtraction returned: ", operation)
    case 3: 
        operation = num1 * num2
        print("Multiplication returned: ", operation)
    case 4: 
        #check if division can be performed
        if num2 == 0:
            print("Error division by zero")
        else: 
            operation = num1 / num2
            print("Division returned: ", operation)
    case _:
        print("Invalid operation")