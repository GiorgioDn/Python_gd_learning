# opens the file in read mode
file = open("python_course/Examples/I_O/test.txt", "r") 

# reads the entire contents of the file
content = file.read()
print(content)

# reads a line from the file 
line = file.readline()
print(line)

# opens the file in write mode, overwriting its contents
file = open("python_course/Examples/I_O/test.txt", "w") 

file.write("Helloooo, maybe")
# closing the file
file.close()

# with 'with open', the file is closed automatically at the end
with open ("python_course/Examples/I_O/test.txt", "r") as file:
    content = file.read()
    print(content)