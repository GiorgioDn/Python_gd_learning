#input variable to select operation type and initial word
start = input("Write a word: ")
cond = input("Write desired operation type for the initial word: add, update, and delete: ")
cond.lower()

#conditions given by input
if cond == "add":
    cond = input("Write the word to add: ")
    print("The new sentence is:", start, cond)
elif cond == "update":
    cond = input("Write word to replace with: ")
    start = cond
    print("The new word is:", start)
elif cond == "delete": 
    start = ""
    print("The word was deleted", start)
else: 
    print("Invalid operation")