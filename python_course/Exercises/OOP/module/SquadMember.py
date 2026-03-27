class TeamMember:
    # the class takes the name as a string and the age as an integer
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
        