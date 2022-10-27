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
fig.show()

