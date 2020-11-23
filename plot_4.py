import math
import numpy as np
from matplotlib import pyplot as plt 

# plot theme
plt.style.use('seaborn')

# to generate list of x values
x = np.arange(-1, +1, 0.01)
# generate list of y values from list of x values
y = x ** 3

# plot x-axis and y-axis
plt.plot(x, y)

# setting title of the plot
plt.title('Cubic Function')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()