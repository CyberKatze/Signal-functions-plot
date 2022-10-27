# %%
import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Iterable


def unit(t):
    if isinstance(t, Iterable):
        return np.array([1 if i >= 0 else 0 for i in t])
    else:
        return 1 if t >= 0 else 0


def ramp(t):
    if isinstance(t, Iterable):
        return np.array([i if i >= 0 else 0 for i in t])
    else:
        return t if t >= 0 else 0

# %%


def Conv(x1, x2):
    def cfunc(n):
        return np.array([sum([x1(k) * x2(i-k) for k in n])for i in n])
    return cfunc


def x1(n): return (2.0)**(n-1) * unit(n)


def s(i): return sum([(np.sin(2*k) + np.exp(2j*np.pi*k/2))*(unit(k+3)-unit(k-5))
                      for k in range(-3, i+1)])


def x2(n): return np.array([s(i) if i < 7 and i > 0 else 0 for i in n])\
    if isinstance(n, Iterable) else (s(n) if n < 7 and n > 0 else 0)


x3 = Conv(x1, x2)

n = np.arange(-3, 20, 1)
gridsize = (3, 1)
fig = plt.figure(figsize=(16, 11))
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax2 = plt.subplot2grid(gridsize, (1, 0))
ax3 = plt.subplot2grid(gridsize, (2, 0))

ax1.stem(n, x1(n), 'b', markerfmt='bo', use_line_collection=True, )
ax1.set_title("$x_1[n]$")
ax2.stem(n, x2(n).real, 'g', markerfmt='go', use_line_collection=True)
ax2.set_title("$|x_2[n]|$")
ax3.stem(n, x3(n).real,'r', markerfmt='ro', use_line_collection=True)
ax3.set_title('|x_1[n]*x_2[n]|')

fig.show()
plt.savefig('doc/images/q5.2.pgf')


# %%
