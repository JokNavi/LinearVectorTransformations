import matplotlib.pyplot as plt
import numpy as np

#Plot 1:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.subplot(1, 2, 1)
plt.plot(x, y,)
plt.title("Plot")

#Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x,y)
plt.title("SubPlot")

plt.suptitle("My plots!")
plt.show()
