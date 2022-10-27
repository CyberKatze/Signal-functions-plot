def x1(n): return (2.0)**(n-1) * unit(n)


def s(i): return sum([(np.sin(2*k) + np.exp(2j*np.pi*k/2))*(unit(k+3)-unit(k-5))
                      for k in range(-3, i+1)])


def x2(n): return np.array([s(i) if i < 7 and i > 0 else 0 for i in n])\
    if isinstance(n, Iterable) else (s(n) if n < 7 and n > 0 else 0)

