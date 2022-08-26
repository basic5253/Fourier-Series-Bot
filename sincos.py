import numpy as np
import matplotlib.pylab as plt

x = np.arange(0, 4*np.pi, 0.5)

plt.plot(x,np.sin(x), marker = "+", label = "sin", linestyle = "-.")
plt.plot(x,np.cos(x), marker = "o", label = "cos" linestyle = ":" )

plt.title("sine and cosine graph")
plt.xlabel("angle")
plt.ylabel("sin & cos values")
plt.legend()
plt.show()