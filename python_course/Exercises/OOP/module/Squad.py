from .SquadMember import TeamMember

class Player(TeamMember):
    # redefine initial attributes
    def __init__(self, name: str, age: int, role: str, jersey_number: int):
        super().__init__(name, age)
        self.role = role
        self.jersey_number = jersey_number
    
    # override the toString method of the superclass
    def __str__(self):
        return f"The player {self.name} of {self.age} years, will play in the role of {self.role}, with jersey number {self.jersey_number}"

    def play_match(self, action: str):
        action = action.lower()
        match action:
            case "shoot":
                print("The player shoots at the goal")
            case "save":
                print("The player saves")
            case "pass":
                print("The player passes to their teammate")
            case _:
                print(f"The player does {action}")

class Coach(TeamMember):
    # redefine initial attributes
    def __init__(self, name: str, age: int, years_of_experience: int):
        super().__init__(name, age)
        self.years_of_experience = years_of_experience
        
    # override the toString method of the superclass
    def __str__(self):
        return f"The coach {self.name} of {self.age} years, with {self.years_of_experience} years of experience"

class Assistant(TeamMember):
    # redefine initial attributes
    def __init__(self, name: str, age: int, specialization: str):
        super().__init__(name, age)
        self.specialization = specialization
    
    # override the toString method of the superclass
    def __str__(self):
        return f"The assistant {self.name} of {self.age} years, is a {self.specialization}"
    
    def support_team(self):
        match self.specialization:
            case "physiotherapist":
                print(f"{self.name} supports the team by making sure everyone is healthy")
            case "game analyst":
                print(f"{self.name} supports the team by making sure they all play well")