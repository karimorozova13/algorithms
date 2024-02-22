import matplotlib.pyplot as plt 
import numpy as np

n = np.arange(1,21)

linear_search_steps = n
binary_search_steps = np.log2(n)

plt.figure(figsize=(10,6))
plt.plot(n, linear_search_steps, label='Linear Search', color='teal')
plt.plot(n, binary_search_steps, label='Binary Search', color='tomato')

plt.xlabel('Number of elements')
plt.ylabel('Number of steps')
plt.title('Comparison of Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()