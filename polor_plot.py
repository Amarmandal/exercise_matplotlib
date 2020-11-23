import numpy as np
from matplotlib import pyplot as plt 

# using plot theme
plt.style.use('seaborn')

# top left corner subplot
fig_1 = plt.subplot(221, projection="polar")

# value of θ in radian 
theta = np.arange(0, 2 * np.pi, 0.01)
# polar equation r = sin^2(θ)
r = np.sin(theta) ** 2

# function to plot value of r and θ
fig_1.plot(theta, r)
# to set outer radical limit
fig_1.set_rmax(1.01)
# radius marker
fig_1.set_rticks([0.5, 1])
# position of marker in degree
fig_1.set_rlabel_position(-22.5)
# plot 1 title
fig_1.set_title("r = sin²(θ)")

# top right corner subplot 
fig_2 = plt.subplot(222, projection="polar")

# polar equation
r2 = np.cos(theta) ** 2
fig_2.plot(theta, r2)
fig_2.set_rmax(1.01)
fig_2.set_rticks([0.5, 1])
fig_2.set_rlabel_position(65.0)
fig_2.set_title("r = cos ^ 2")

# bottom left corner subplot with rectilinear plot type
fig_3 = plt.subplot(223, projection="rectilinear")

# value of x
x = np.arange(-1, 1, 0.01)
# value of y
y = x ** 2

fig_3.plot(x, y)
fig_3.set_title("Plot: y = x ^ 2")
fig_3.set_xlabel("X-axis")
fig_3.set_ylabel("Y-axis")

fig_4 = plt.subplot(224, projection="rectilinear")

x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)

fig_4.plot(x, y)

fig_4.set_title("Sine Function")
fig_4.set_xlabel("Angle in radian")
fig_4.set_ylabel("Value of y")



# to fix spacing and padding issue
plt.tight_layout()

# display all the plot
plt.show()
# plt.savefig('plot.png')