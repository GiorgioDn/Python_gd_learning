import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#create empty figure
plt.figure()
#set x and y coordinates
plt.plot(x, y)
#graph title
plt.title('Line Plot')
#x axis name
plt.xlabel('X Axis')
#y axis name
plt.ylabel('Y Axis')
#display graph
plt.show()

#create bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

#histogram
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()