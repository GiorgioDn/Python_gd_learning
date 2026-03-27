#initialize the age variable of type int which will be chosen by the user
age = int(input("Write your age: "))

#compare age
if age>=18 and age<105:
    print("You can see this movie")
elif age<0 or age>105:
    print("Invalid age")
else:
    print("Sorry, you can't see this movie")