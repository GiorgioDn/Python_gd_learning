#user number selection to populate the list
list_num = []
print ("Select numbers")
#add inputs to the list as they are typed by the user
num = float(input("First number: "))
list_num.append(num)
num = float(input("Second number: "))
list_num.append(num)
num = float(input("Third number: "))
list_num.append(num)
num = float(input("Fourth number: "))
list_num.append(num)
num = float(input("Fifth number: "))
list_num.append(num)

#I write available operations and let user choose
print("Select the corresponding operation number: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
operation = int(input())

#associate corresponding operation based on user input
match operation:
    case 1: 
        operation = list_num[0] + list_num[1] + list_num[2] + list_num[3] + list_num[4]
        print("Addition returned: ", operation)
    case 2: 
        operation = list_num[0] - list_num[1] - list_num[2] - list_num[3] - list_num[4]
        print("Subtraction returned: ", operation)
    case 3: 
        operation = list_num[0] * list_num[1] * list_num[2] * list_num[3] * list_num[4]
        print("Multiplication returned: ", operation)
    case 4: 
        #check if division can be performed
        if list_num[0] == 0 or list_num[1] == 0 or list_num[2] == 0 or list_num[3] == 0 or list_num[4] == 0:
            print("Error division by zero")
        else: 
            operation = list_num[0] / list_num[1] / list_num[2] / list_num[3] / list_num[4]
            print("Division returned: ", operation)
    case _:
        print("Invalid operation")