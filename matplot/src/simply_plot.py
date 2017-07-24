import numpy as np
import matplotlib.pyplot as plt


def plot_function_name(name, x=0, y=0):
    plt.text(x, y, name, alpha=0.3, size=25, ha="center", va="center")

xmin, xmax = -np.pi, np.pi
x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('$\sin(x)$')
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)
plot_function_name('$\sin(x)$')

plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('$\cos(x)$')
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)
plot_function_name('$\cos(x)$')

plt.tight_layout()
plt.show()

