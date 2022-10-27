# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import scipy.integrate as integrate
from collections.abc import Iterable
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


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


def X(t):
    return ((-ramp(t+2) * unit(-t-1)) +
            (ramp(2*t+2) - 1) * (unit(t+1)-unit(t)) +
            (unit(t) - unit(t-2)))

# %%


def S(x):
    def y(t):
        return np.array([integrate.quad(lambda u: x(u-2)*np.exp(u-i), -20, 20)[0] for i in t])
    return y


def x1(t): return unit(t) - unit(t-2)


def x2(t): return unit(t) - unit(t-3)


a1 = 3
a2 = 2


def s1(t): return S(lambda n: a1*x1(n) + a2*x2(n))(t)


def s2(t): return S(lambda n: a1*x1(n))(t) + S(lambda n: a2*x2(n))(t)


# sampling with rate 100 per second
t = np.linspace(-5, 5, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(t, s1(t))
ax2.plot(t, s2(t))

#plt.savefig('doc/images/q3.1.pgf')
# %%


def y1(t): return S(x1)(t)


def y2(t): return S(lambda n: x1(n-3))(t)


# sampling with rate 100 per second
t = np.linspace(-5, 5, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(t, y1(t-3))
ax2.plot(t, y2(t))
plt.savefig('doc/images/q3.2.pgf')
fig.show()
# %%
