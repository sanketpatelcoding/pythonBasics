from html.parser import charref

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style



# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]
# plt.figure(figsize=(6, 4))  # Set figure size
# # Red line
# plt.plot(x, y, color='red', linewidth=2)
# plt.title('sanket 1st Plot')
# plt.xlabel('X-ax')
# plt.ylabel('Y-ax')
# # for the grid
# plt.grid(True)
# plt.legend()
# plt.show()


# 2. two graphs in One
x = np.array([1, 2, 3, 4, 5])
# y1 = x**2  # First line: x squared
# y2 = x**3  # Second line: x cubed
# plt.figure(figsize=(6, 4))
# plt.plot(x, y1, color='blue', label='square')
# plt.plot(x, y2, color='green', label='cube')
# plt.title('Multiple Lines in One Plot')
# plt.xlabel('X-axis for number')
# plt.ylabel('Y-axis for their square and cube')
# plt.legend()
# plt.grid(True)
# plt.show()


# 3bar charre
# players = ['Rohit', 'Kohli', 'Pandya', 'Gill', 'Sharma']
# scores = [82, 54, 66, 42, 74]
#
# style.use('ggplot')
#
# plt.bar(players, scores, color='teal')
# plt.show()

# 4scatter
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='purple', s=10)
# s is scaller to cnortol size of marked point
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()