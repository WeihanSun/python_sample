import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(211)
p1 = ax1.plot(x, y_sin, 'r', label="sin")
plt.legend(loc="lower right")
ax2 = fig1.add_subplot(212)
p2 = ax2.plot(x, y_cos, 'b', label="cos")
plt.legend(loc="upper right")

fig2 = plt.figure(2)
p1, = plt.plot(x, y_sin, 'r')
p2, = plt.plot(x, y_cos, 'g')
plt.legend([p1, p2], ["sin", "cos"])

fig3 = plt.figure(3)
ax1 = fig3.add_subplot(211)
ax2 = fig3.add_subplot(212)
p1, = ax1.plot(x, y_sin, 'r')
p2, = ax2.plot(x, y_cos, 'b')
ax1.legend([p1], ["sin"], loc="lower right")
ax2.legend([p2], ["ocs"], loc='upper right')
plt.show()
