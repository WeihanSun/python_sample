# base class: Artist
# 2nd children: figure, lines, patch, text axis

import numpy as np
import matplotlib.pyplot as plt

# figure 1: sin & cos
xmin, xmax = -np.pi, np.pi
x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# different from simply_plot
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(211)
ax2 = fig1.add_subplot(212)
p1 = ax1.plot(x, y_sin, label="sin")
p2 = ax2.plot(x, y_cos, label="cos")
ax1.set_title('$\sin(x)$')
ax2.set_title('$\cos(y)$')
ax1.set_ylim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)
ax1.set_xlabel("x")
ax2.set_xlabel("x")

fig1.tight_layout()
#fig.show()  # disappear immediately

# figure 2 : share the same y
n = 300
x = np.random.randn(n)
y1 = np.exp(x) + np.random.randn(n)
y2 = np.exp(x) * 3 + np.random.randn(n)

fig2 = plt.figure(2)
ax1 = fig2.add_subplot(121)
ax2 = fig2.add_subplot(122, sharey=ax1)

ax1.plot(x, y1, ".")
ax2.plot(x, y2, ".")

# figure 3 : share the same x
n = 300
x = np.random.randn(n)
y = np.sin(x) + np.random.randn(n) * 0.3

fig3 = plt.figure(3)

# サブプロットを8:2で分割
ax1 = fig3.add_axes((0.1, 0.3, 0.8, 0.6))  # left-bottom = (0,0)
ax2 = fig3.add_axes((0.1, 0.1, 0.8, 0.2), sharex=ax1)  # specify (x, y, w, h)

# 散布図のx軸のラベルとヒストグラムのy軸のラベルを非表示
ax1.tick_params(labelbottom="off")
ax2.tick_params(labelleft="off")

ax1.plot(x, y, "x")
ax2.hist(x, bins=20)

plt.show()

