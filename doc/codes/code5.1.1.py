def Conv(x1, x2):
    def cfunc(n):
        return np.array([sum([x1(k) * x2(i-k) for k in n])for i in n])
    return cfunc
