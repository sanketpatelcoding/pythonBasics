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
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 5, 4, 5]
# plt.figure(figsize=(6, 4))
# plt.scatter(x, y, color='purple', s=10)
# # s is scaller to cnortol size of marked point
# plt.title('Scatter Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()


# --------------------------------------------------------

# plt.xlabel(), plt.ylabel(): Set the x-axis and y-axis labels.
# plt.title(): Set the title of the plot.
# plt.legend(): Add a legend to the plot.
# plt.grid(): Add a grid to the plot.
#
# Subplots:
# plt.subplot(): Create subplots.
# plt.subplots(): Create multiple subplots.
# plt.figure(): Create a figure for the plot.
#
# Text and Annotations:
# plt.text(): Add text to the plot.
# plt.annotate(): Annotate specific points on the plot.


#
#np concept from internet
# x = np.array([1, 2, 3, 4])
# y1 = np.array([10, 20, 25, 30])
# y2 = np.array([40, 10, 30, 20])
# plt.figure(figsize=(6, 4))
# plt.plot(x, y1, color='red', label='Line 1')
# plt.plot(x, y2, color='blue', label='Line 2')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Line Plot with Legend and Grid')
# plt.legend()
# plt.grid(True)
# plt.show()
# explain:(6, 8) means the 6 inches wide and 8 inches tall.
# x = np.array([1, 2, 3, 4])
# y = np.array([10, 20, 25, 30])
# # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 8))
# # ax1=plt.subplot(121)
# ax1=plt.subplot(211)
# ax1.plot(x, y, color='blue')
# ax1.set_title('line graph')
# ax1.set_xlabel('X-axis')
# ax1.set_ylabel('Y-axis')
# ax1.grid(True)
# # ax2=plt.subplot(122)
# ax2=plt.subplot(212)
# # for scatter
# # =================================================
# ax2.scatter(x, y, color='purple', s=100, marker='x')
# ax2.set_title('Scatter Plot')
# ax2.set_xlabel('X-axis')
# ax2.set_ylabel('Y-axis')
# ax2.grid(True)
# plt.tight_layout()
# plt.show()
#
# x = np.array([1, 2, 3, 4])
# y = np.array([10, 20, 25, 30])
# plt.figure(figsize=(6, 4))
# plt.scatter(x, y, color='purple', s=100, marker='o')
# plt.text(4, 30, 'Max Value', fontsize=12, color='black')
# plt.annotate('Peak', xy=(3, 25), xytext=(2, 28),
#  arrowprops=dict(facecolor='black', shrink=0.1))
# plt.title('Scatter Plot with Text and Annotation')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()


# # histog
# hours_studied = [5, 10, 15, 8, 20, 12, 25, 30, 18, 22, 7, 14, 28, 16, 9, 11, 19, 24]
# bins = [0, 5, 10, 15, 20, 25, 30, 35]
#
#
# plt.hist(hours_studied, bins=bins, histtype='bar', color='black', edgecolor='darkblue', rwidth=0.8)
# plt.xlabel('hours Studied in one week')
# plt.ylabel('Num of Student')
# plt.title('weekly study hours graph')
#
#
# plt.grid()
# plt.tight_layout()
#
# plt.show()


height = np.array([125, 138, 144, 193, 180, 176, 155, 183, 172, 140, 139])
weight = np.array([66, 82, 72, 88, 70, 90, 60, 79, 64, 55, 66])
bmi = weight / ((height / 100) ** 2)
# ax = plt.axes(projection='3d')
# ax.scatter(height, weight)
# plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(height, weight, bmi, c='blue')

# Labels
ax.set_xlabel('height')
ax.set_ylabel('weight')
ax.set_zlabel('bmi')

# Show plot
plt.show()