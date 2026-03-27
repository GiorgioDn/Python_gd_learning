from .module.Student import Student
from .module.Professor import Professor

while True:
    
    grades = []
    
    print("Type the student's name and age")
    name = input("Name: ")
    age = int(input("Age: "))
    
    while True:
        print("Enter the student's grade: ")
        grade = int(input("Grade: "))
        
        grades.append(grade)
        
        choice = input("Do you want to enter another grade? ")
    
        if choice.lower() == "no":
            break
        
    student = Student(name, age, grades)
    
    if student.get_name() == False or student.get_age() == False:
        if student.get_name() == False:
            name = input("invalid name, type a new name: ")
            student.set_name(name)
        else:
            age = int(input("invalid age, type a new age: "))
            student.set_age(age)
    
    print(student.presentation())
        
    print("Type the name, age, and subject of the professor")
    name = input("Name: ")
    age = int(input("Age: "))
    subject = input("Subject: ")
    
    professor = Professor(name, age, subject)
    
    if professor.get_name() == False or professor.get_age() == False or professor.get_subject() == False:
        if professor.get_name() == False:
            name = input("invalid name, type a new name: ")
            professor.set_name(name)
        elif professor.get_subject() == False:
            subject = input("invalid subject, type a new subject: ")
            professor.set_subject(subject)
        else:
            age = int(input("invalid age, type a new age: "))
            professor.set_age(age)
    
    print(professor.presentation())
    
    choice = int(input("Select what to do with the student: \n1. Add grade\n2. Calculate average\n"))
    
    match choice:
        case 1:
            grade = int(input("Add the grade: "))
            student.add_grade(grade)
            print(f"The student's grades are: {student.get_grades()}")
        case 2: 
            average = student.calculate_average()
            print(f"The student's average is {average}")
        case _:
            print("Invalid choice")
    
    choice = input("Do you want to perform a new test? ")
    
    if choice.lower() == "no":
        break