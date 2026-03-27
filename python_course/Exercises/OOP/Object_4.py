# instantiate a restaurant class
class Restaurant:
    
    # class attributes
    # indicates opening status
    open = False
    # dictionary containing the menu
    
    menu = {}
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    # method describes the restaurant
    def describe_restaurant(self):
        print(f"The restaurant {self.name} specializes in {self.cuisine_type}")
        
    # method that shows opening status based on open attribute
    def opening_status(self):
        if self.open == True:
            print("The restaurant is open")
        else:
            print("The restaurant is closed")
        
    # method to open the restaurant and set open to true
    def open_restaurant(self):
        if self.open == True:
            self.opening_status()
        else: 
            self.open = True
            print("The restaurant is now open")
         
    # method to close the restaurant and set open to false   
    def close_restaurant(self):
        if self.open == False:
            self.opening_status()
        else: 
            self.open = False
            print("The restaurant is now closed")
            
    # method to add to menu
    def add_to_menu(self, dish_name, price):
        self.menu[dish_name] = price
    
    # method to remove from menu
    def remove_from_menu(self, dish_name):
        self.menu.pop(dish_name)
        
    # method to print the menu items
    def print_menu(self):
        print("The menu is as follows: ")
        for k, v in self.menu.items():
            print(f"{k} : {v}")

while True:
    
    # declare the restaurant
    print("Type the name of the restaurant and the type of cuisine you want to add")
    name = input("Restaurant name: ")
    cuisine_type = input("Cuisine type: ")
    
    restaurant = Restaurant(name, cuisine_type)
    
    restaurant.describe_restaurant()
    
    restaurant.opening_status()
    
    # create dishes to add to the menu
    print("Add types of dishes with their relative prices to the menu")
    while True:
        dish_name = input("Dish name: ")
        price = float(input("Price: "))
        
        restaurant.add_to_menu(dish_name, price)
        
        choice = input("Do you want to add more dishes? ")
        # exit the while loop
        if choice.lower() == "no":
            break
    
    restaurant.print_menu()
    
    # choose one of the methods to use
    choice = int(input("Select the operation to perform: \n1. Add to menu \n2. Remove from menu \n3. Modify opening \n4. Print menu\n"))
    
    match choice:
        case 1:
            print("Add dish types with their prices to the menu")
            dish_name = input("Dish name: ")
            price = float(input("Price: "))
        
            restaurant.add_to_menu(dish_name, price)
            
            restaurant.print_menu()
        case 2:
            print("Remove the dish")
            dish_name = input("Dish name: ")
            
            restaurant.remove_from_menu(dish_name)
            
            restaurant.print_menu()
        case 3:
            choice = input("Select if the restaurant is open or closed: ")
            if choice.lower() == "open":
                restaurant.open_restaurant()
            else: 
                restaurant.close_restaurant()
        case 4:
            restaurant.print_menu()
        case _:
            print("Operation not available")
    
    choice = input("Do you want to repeat the choice? ")
    # exit the while loop
    if choice.lower() == "no":
        break