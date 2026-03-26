# create a dictionary by associating it with a variable
student = {
    "name": "Alice",
    "age": 20,
    "gender": "female",
}

# return the dictionary data
print(student["name"])
print(student["age"])

# modify the age value
student["age"] = 21
print(student)

# add an element
student["city"] = "Rome"
print(student)

# print only the keys
print(student.keys())

# print only the values
print(student.values())

# print the list of key-value pairs
print(student.items())

# print the value associated with a key
print(student.get("name"))
