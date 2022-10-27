# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from collections.abc import Iterable
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


# %%
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


gridsize = (2, 1)
fig = plt.figure(figsize=(20, 15))
# sampling with rate: 10 sample per second
t1 = np.linspace(-0.5, 0.5, 10)
# settings for axes1
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax1.set_xticks(np.arange(-1, 1, step=0.1))
ax1.set_title('$u(t)$ with sampling rate of $F_s =10$', fontsize=20)

# sampling with rate: 100 sample per second
t2 = np.linspace(-0.5, 0.5, 100)
# settings for axes2
ax2 = plt.subplot2grid(gridsize, (1, 0))
ax2.set_xticks(np.arange(-1, 1, step=0.1))
ax2.set_title('$u(t)$ with sampling rate of $F_s =100$', fontsize=20)

#plot and show
ax1.plot(t1, unit(t1), '.-')
ax2.plot(t2, unit(t2), '.-')
# plt.savefig('doc/images/unit.pgf')
fig.show()


# %%
gridsize = (2, 1)
fig = plt.figure(figsize=(20, 15))
# sampling with rate: 10 sample per second
t1 = np.linspace(-0.5, 0.5, 10)
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax1.set_xticks(np.arange(-1, 1, step=0.1))
ax1.set_title('$r(t)$ with sampling rate of $F_s =10$', fontsize=20)

# sampling with rate: 100 sample per second
t2 = np.linspace(-0.5, 0.5, 100)
ax2 = plt.subplot2grid(gridsize, (1, 0))
ax2.set_xticks(np.arange(-1, 1, step=0.1))
ax2.set_title('$r(t)$ with sampling rate of $F_s =100$', fontsize=20)

#plot and show
ax1.plot(t1, ramp(t1), '.-')
ax2.plot(t2, ramp(t2), '.-')
# plt.savefig('doc/images/ramp.pgf')
fig.show()

# %%


def x1(t): return -ramp(t+2) * unit(-t-1)


def x2(t): return (ramp(2*t+2) - 1) * (unit(t+1)-unit(t))


def x3(t): return unit(t) - unit(t-2)


def x(t): return x1(t)+x2(t)+x3(t)


# sampling with rate : 100 sample per second
t = np.linspace(-5, 5, 1000)

# Figure settings
gridsize = (3, 3)
fig = plt.figure(figsize=(10, 10))
axs = []
axs.append(plt.subplot2grid(gridsize, (0, 0), rowspan=2, colspan=3))
axs.append(plt.subplot2grid(gridsize, (2, 0)))
axs.append(plt.subplot2grid(gridsize, (2, 1)))
axs.append(plt.subplot2grid(gridsize, (2, 2)))
for i in range(4):
    axs[i].set_xticks(np.arange(-4, 5, step=1))
    axs[i].set_title(
        f'$x{"_"+str(i) if i>0 else "=x_1 + x_2 + x_3"}$', fontsize=16)


#plot and show
axs[0].plot(t, x(t))
axs[1].plot(t, x1(t))
axs[2].plot(t, x2(t))
axs[3].plot(t, x3(t))
# plt.savefig('doc/images/x.pgf')
fig.show()


# %%
def y1(t): return x(2*t+2)


fig, ax = plt.subplots(1, 1)

#plot and show
ax.plot(t, y1(t))
# plt.savefig('doc/images/y1.pgf')

fig.show()

# %%


def y2(t): return x(-t+1)


fig, ax = plt.subplots(1, 1)

#plot and show
ax.plot(t, y2(t))
# plt.savefig('doc/images/y2.pgf')
fig.show()
