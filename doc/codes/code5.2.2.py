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
