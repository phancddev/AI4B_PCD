import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
data1 = [3, 7, 5, 2]
data2 = [4, 6, 3, 8]

x = np.arange(len(categories))
width = 0.35

plt.bar(x - width/2, data1, width, label='Data 1', color='blue')
plt.bar(x + width/2, data2, width, label='Data 2', color='orange')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.xticks(x, categories)
plt.legend()

plt.show()
