#definisco la funzione per la funzione filtro 
def is_even(x):
    return x%2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#uso la funzione filter applicando la funzione all'elemento iterabile
even_numbers = list(filter(is_even, numbers))
print(even_numbers)