# import matplotlib.pyplot as plt
# fig,a =  plt.subplots(2,2)
# import numpy as np
# x = np.arange(1,5)
# a[0][0].plot(x,x*x)
# a[0][0].set_title('square')
# a[0][1].plot(x,np.sqrt(x))
# a[0][1].set_title('square root')
# a[1][0].plot(x,np.exp(x))
# a[1][0].set_title('exp')
# a[1][1].plot(x,np.log10(x))
# a[1][1].set_title('log')
# plt.show()

from matplotlib import pyplot as plt 
import numpy as np

plt.style.use('seaborn')

fig, a = plt.subplots(2, 2)

x = np.arange(-1, 1, 0.01)

plot_1 = a[0][0]
plot_2 = a[0][1]
plot_3 = a[1][0]
plot_4 = a[1][1]

plot_1.plot(x, x ** 2)
plot_2.plot(x, x ** 3)
plot_3.plot(x, 5*x - 1)
plot_4.plot(x, x ** 4)


plot_1.set_title('Square Curve')
plot_2.set_title('Cubic Curve')
plot_3.set_title('Sine Funciton')
plot_4.set_title('Cosine Function')

plt.show()