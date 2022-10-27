# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


def unit(t): return np.array([1 if i >= 0 else 0 for i in t])


def ramp(t): return np.array([i if i >= 0 else 0 for i in t])


def x1(t): return -ramp(t+2) * unit(-t-1)


def x2(t): return (ramp(2*t+2) - 1) * (unit(t+1)-unit(t))


def x3(t): return unit(t) - unit(t-2)


def x(t): return x1(t)+x2(t)+x3(t)


# %% 2.1
def x_o(n): return(x(n)-x(-n))/2


def x_e(n): return (x(n)+x(-n))/2


def x_i(n): return np.array([x(np.array([i]))[0] if i < 0 else 0 for i in n])


def x_r(n): return np.array([x(np.array([i]))[0] if i >= 0 else 0 for i in n])


# sampling with rate : 100 sample per second
t = np.linspace(-2.5, 2.5, 500)

# Figure settings
gridsize = (2, 2)
fig = plt.figure(figsize=(10, 10))
axs = []
axs.append(plt.subplot2grid(gridsize, (0, 0)))
axs.append(plt.subplot2grid(gridsize, (0, 1)))
axs.append(plt.subplot2grid(gridsize, (1, 0)))
axs.append(plt.subplot2grid(gridsize, (1, 1)))
for i in range(4):
    axs[i].set_xticks(np.arange(-4, 5, step=1))
axs[0].set_title(f'$x_o[n]$', fontsize=16)
axs[1].set_title(f'$x_e[n]$', fontsize=16)
axs[2].set_title(f'$x_i[n]$', fontsize=16)
axs[3].set_title(f'$x_r[n]$', fontsize=16)

#plot and show
axs[0].plot(t, x_o(t), 'ro', c='blue', markersize=1)
axs[1].plot(t, x_e(t), 'ro', c='red', markersize=1)
axs[2].plot(t, x_i(t), 'ro', c='green', markersize=1)
axs[3].plot(t, x_r(t), 'ro', c='purple', markersize=1)
#plt.savefig('doc/images/q2.1.pgf')
fig.show()

# %% 2.2


def z(t):
    # negative t
    tn = np.array([i for i in t if i < 0])
    # positive t
    tp = np.array([i for i in t if i >= 0])

    neg = 2*x_e(tn) - x_r(-tn)
    pos = x_r(tp)
    return np.concatenate((neg, pos))


# Figure settings
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.set_title("$z[n]$")
ax2.set_title('$x[n]$')

#plot and show
ax1.plot(t, z(t), 'ro', c='red', markersize=1)
ax2.plot(t, x(t), 'ro', c='blue', markersize=1)
#plt.savefig('doc/images/q2.2.pgf')
fig.show()
# %% 2.3
def q(t):
    # negative t
    tn = np.array([i for i in t if i < 0])
    # positive t
    tp = np.array([i for i in t if i >= 0])

    neg = x_i(tn)
    pos = 2*x_o(tp) + x_i(-tp)
    return np.concatenate((neg, pos))


# Figure settings
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.set_title("$q[n]$")
ax2.set_title('$x[n]$')

#plot and show
ax1.plot(t, q(t), 'ro', c='green', markersize=1)
ax2.plot(t, x(t), 'ro', c='blue', markersize=1)
#plt.savefig('doc/images/q2.3.pgf')
fig.show()
