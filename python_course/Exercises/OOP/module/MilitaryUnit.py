class MilitaryUnit:
    withdrawn = False
    # takes a string name and an integer soldier count as input
    def __init__(self, name: str, soldier_count: int):
        self.name = name
        self.soldier_count = soldier_count
    # method that takes a position as input
    def move(self, position: str):
        print(f"The unit has moved to {position}")
    # method that takes a target as input
    def attack(self, target: str):
        print(f"The unit attacks {target}")
    def withdraw(self):
        self.withdrawn = True
        return self.withdrawn