# %%
def y2(t): return x(-t+1)

fig, ax = plt.subplots(1, 1)

#plot and show
ax.plot(t, y2(t))
#plt.savefig('doc/images/y2.pgf')
fig.show()

