gridsize = (2, 1)
fig = plt.figure(figsize=(20, 15))
# sampling with rate: 10 sample per second
t1 = np.linspace(-0.5, 0.5, 10)
# settings for axes1
ax1 = plt.subplot2grid(gridsize, (0, 0))
ax1.set_xticks(np.arange(-1, 1, step=0.1))
ax1.set_title("$u(t)$ with sampling rate of $F_s =10$", fontsize=20)

# sampling with rate: 100 sample per second
t2 = np.linspace(-0.5, 0.5, 100)
# settings for axes2
ax2 = plt.subplot2grid(gridsize, (1, 0))
ax2.set_xticks(np.arange(-1, 1, step=0.1))
ax2.set_title("$u(t)$ with sampling rate of $F_s =100$", fontsize=20)

#plot and show
ax1.plot(t1, unit(t1), '.-')
ax2.plot(t2, unit(t2), '.-')
#plt.savefig('doc/images/unit.pgf')
fig.show()

