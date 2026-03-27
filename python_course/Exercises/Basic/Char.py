#get the input word
str_in = input("Type a word: ")
str_out = ""

#get each character with a space acting as a delimiter
for s in str_in:
    str_out += s + " "

#print each character separated by spaces
print(str_out)