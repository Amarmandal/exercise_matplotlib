import numpy as np
from matplotlib import pyplot as plt 

plt.style.use('seaborn')

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection="polar")
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
# ax.set_rticks(np.arange(0.5, 4.5, 0.5))
ax.set_rlabel_position(-22.5)
ax.grid(True)

ax.set_title('A line plot on a polar axis', va='bottom')
plt.show()

# for i in range(20):
#     print(f"{r[i]}, {theta[i]}")


