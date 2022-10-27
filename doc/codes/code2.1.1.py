def x_o(n): return(x(n)-x(-n))/2


def x_e(n): return (x(n)+x(-n))/2


def x_i(n): return np.array([x(np.array([i]))[0] if i < 0 else 0 for i in n])


def x_r(n): return np.array([x(np.array([i]))[0] if i >= 0 else 0 for i in n])

