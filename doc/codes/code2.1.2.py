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
fig.show()

