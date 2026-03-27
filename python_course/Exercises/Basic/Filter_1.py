numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
#filter test
def sum_elem(x, list): 
    for i in range(len(list)-2):
        return list[x] + list[x + 1] > list[x + 2]

index = []
for i in range(len(numbers)-2):
    index.append(i)

valid_index = list(filter(sum_elem(index, numbers), index))

valid_group = [
    (numbers[i], numbers[i + 1], numbers[i + 2])
    for i in valid_index
]


print("Indices that meet the condition:", valid_index)
print("Valid groups (x, x+1, x+2):", valid_group)
'''

#filter function: takes an index x
def sum_two_greater_than_third(x):
    return numbers[x] + numbers[x + 1] > numbers[x + 2]

indici = range(len(numbers) - 2)

valid_index = list(filter(sum_two_greater_than_third, indici))

valid_group = [
    (numbers[i], numbers[i + 1], numbers[i + 2])
    for i in valid_index
]

print("Indices that meet the condition:", valid_index)
print("Valid groups (x, x+1, x+2):", valid_group)