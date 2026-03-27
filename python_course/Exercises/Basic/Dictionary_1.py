#dictionary data input
boolean = input("Enter a boolean value: ")
integer = int(input("Enter an integer: "))
string = input("Enter the string: ")

#dictionary with input values
diz = {
    "boolean": boolean,
    "integer": integer,
    "string": string,
}

#list of dictionaries
list_diz = [diz]

#dictionary with list
date = {
    
    "datatype": [boolean, integer, string],
    "dictionary": list_diz
    
}

#display keys and values
for x, y in diz.items():
    print("key: ", x)
    print("value: ", y)