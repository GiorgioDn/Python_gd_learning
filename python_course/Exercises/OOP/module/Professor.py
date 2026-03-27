from .Person import *

class Professor(Person):
    # takes superclass values and a string as input
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.__subject = subject
     
    # use getters to access the corresponding parameters   
    def get_subject(self):
        if len(self.__subject) > 0:
            return self.__subject
        else:
            return False
    
    # use setters to modify parameters
    def set_subject(self, subject: str):
        if len(subject) > 0:
            self.__subject = subject
        else:
            return False
    
    # overridden introduction method
    def introduction(self):
        base = super().introduction()
        return f"The professor {base} and teaches the following subject: {self.__subject}"