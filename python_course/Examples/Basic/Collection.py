#creating tuples
point = (3, 4)
color_rgb = (255, 128, 0)
person_information = ("Alice", 25, "Female")

#print of the elements
print(point[0])
print(point[1])

#packing tuple
point = 1, 4
#unpacking tuple
x, y= point
#print variables
print(x, y)

#creating sets
#conversion lists to sets
set1 = set([1, 2, 3, 4, 5])
#creating sets
set2 = {5, 6, 7, 8, 9}
set3 = {1, 2, 3, 3, 4, 4, 5}
#don't print duplicates
print(set3)

#union operation: returns the values from both sets
set4 = set1.union(set2)
print(set4)
#intersection operation: returns the common values from the sets
set4 = set1.intersection(set2)
print(set4)
#difference operation: returns the values not present in the other set
set4 = set1.difference(set2)
print(set4)
#symmetric difference operation: returns the unique values from each set
set4 = set1.symmetric_difference(set2)
print(set4)

#add: adds an element
colors = {"red", "blue"}
colors.add("green")
print(colors)
#remove: removes the element, raises an error if the element is not present
colors.remove("green")
print(colors)
#discard: like remove, but without error
colors.remove("red")
print(colors)
#len: returns the length of the set
print(len(set2))
#copy: copies the set
set4 = set1.copy()
print(set4)