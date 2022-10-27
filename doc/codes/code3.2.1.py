def y1(t): return S(x1)(t)


def y2(t): return S(lambda n: x1(n-3))(t)
