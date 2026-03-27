# list containing the numbers to sum
sum_num=[]

while True:
    print("Choose integer numbers, enter 0 to finish")
    
    # variable to allow the user to enter infinite numbers
    end_number = 1
    # update the list with each number until 0 is chosen
    while end_number !=0:
        num = int(input("Choose a number: "))
        sum_num.append(num)
        end_number = num
    
    # when the final number is 0, sum the numbers
    if end_number == 0:
        total_sum = 0
        n = 0
        while n<len(sum_num):
            total_sum += sum_num[n]
            n+=1 
        # print and exit the loop
        print("The sum of the numbers is:", total_sum)
        break