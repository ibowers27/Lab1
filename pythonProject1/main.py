# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt

x_coord = [1, 2, 5, 10, 20]
y_coord = [1, 2, 3, 4, 5]

plt.plot([x_coord], [y_coord], 'md')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()