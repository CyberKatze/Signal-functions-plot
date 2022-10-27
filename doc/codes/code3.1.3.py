# sampling with rate 100 per second
t = np.linspace(-5, 5, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(t, s1(t))
ax2.plot(t, s2(t))

