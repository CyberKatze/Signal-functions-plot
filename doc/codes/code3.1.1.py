def S(x):
    def y(t):
        return np.array([integrate.quad(
            lambda u: x(u-2)*np.exp(u-i), -20, 20)[0] for i in t])
    return y
