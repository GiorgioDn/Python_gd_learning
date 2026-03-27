from .module.Squad import *

while True:
    
    print("Enter the player's name, age, role, and jersey number")
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    jersey_number = int(input("Jersey number: "))
    
    player = Player(name, age, role, jersey_number)
    
    print(player)
    
    action = input("Enter the action: shoot, save, or pass: ")
    
    player.play_match(action)
    
    print("Enter the coach's name, age, and years of experience")
    name = input("Name: ")
    age = int(input("Age: "))
    years = input("Years of experience: ")
    
    coach = Coach(name, age, years)
    
    print(coach)
    
    print("Enter the assistant's name, age, and specialization (physiotherapist or game analyst)")
    name = input("Name: ")
    age = int(input("Age: "))
    specialization = input("physiotherapist or game analyst: ")
    
    assistant = Assistant(name, age, specialization)
    
    print(assistant)
    
    assistant.support_team()
    
    choice = input("Do you want to repeat the choice? ")
    
    # exit the while loop
    if choice.lower() == "no":
        break