from .Person import *

class Student(Person):
    # takes superclass values and a list of integers as input
    def __init__(self, name: str, age: int, grades: list[int]):
        super().__init__(name, age)
        self.__grades = grades
    
    # use getters to access the corresponding parameters
    def get_grades(self):
        if len(self.__grades) > 0:
            return self.__grades
        else:
            return False
    
    # use setters to modify parameters
    def set_grades(self, grades: list[int]):
        if len(grades) > 0:
            self.__grades = grades
        else:
            return False
    
    # method to add a single grade
    def add_grade(self, grade: int):
        if grade > 0 and grade <= 10:
            self.__grades.append(grade)
        else:
            return False
    
    # method to calculate average
    def calculate_average(self):
        total = 0
        count = len(self.__grades)
        if count > 0:
            for grade in self.__grades:
                total += grade
            average = total / count
            return average
        else:
            return False
    
    # overridden introduction method
    def introduction(self):
        base = super().introduction()
        return f"The student {base} and the following grades: {self.__grades}"