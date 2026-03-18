#prendo la parola in input
str_in = input("Digitare una parola: ")
str_out = ""

#prendo il singolo char con lo spazio che farà da delimitatore
for s in str_in:
    str_out += s + " "

#stampo ogni singola parola spaziandole    
print(str_out)