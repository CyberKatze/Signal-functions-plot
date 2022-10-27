# %%
def y1(t): return x(2*t+2)


fig, ax = plt.subplots(1, 1)

#plot and show
ax.plot(t, y1(t))
fig.show()

