# define the Point class
class Point:
    # define the constructor method that takes the point's coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # move method: changes the coordinates
    def move(self, dx, dy):
        self.x = dx 
        self.y = dy
    # distance from origin method: calculates the distance between the point and the origin
    def distance_from_origin(self):
        distance = (self.x**2 + self.y**2)**0.5
        return distance

while True:
    # input data to instantiate the class
    print("Select the coordinates of the point")
    x = int(input("Point x: "))
    y = int(input("Point y: "))
    
    point = Point(x, y)
    
    choice = int(input("Which operation do you want to perform: \n1. Print coordinates \n2. Move coordinates \n3. Distance from origin\n"))
    
    # choice of methods declared in the class
    match choice:
        case 1:
            print(f"Coordinate x = {point.x} \nCoordinate y = {point.y}")
        case 2:
            print("Select the new coordinates of the point")
            x = int(input("Point x: "))
            y = int(input("Point y: "))
            point.move(x, y)
            print(f"New coordinate x = {point.x} \nNew coordinate y = {point.y}")
        case 3:
            distance = point.distance_from_origin()
            print(f"The distance from the origin is: {distance}")
        case _:
            print("Invalid choice")
    
    choice = input("Do you want to repeat the choice? ")
    
    # exit the while loop
    if choice.lower() == "no":
        break