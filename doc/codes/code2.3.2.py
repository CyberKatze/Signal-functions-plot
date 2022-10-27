# Figure settings
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.set_title("$q[n]$")
ax2.set_title('$x[n]$')

#plot and show
ax1.plot(t, q(t), 'ro', c='green', markersize=1)
ax2.plot(t, x(t), 'ro', c='blue', markersize=1)
plt.savefig('doc/images/q2.3.pgf')
fig.show()
