def x1(t): return unit(t) - unit(t-2)


def x2(t): return unit(t) - unit(t-3)


a1 = 3
a2 = 2


def s1(t): return S(lambda n: a1*x1(n) + a2*x2(n))(t)


def s2(t): return S(lambda n: a1*x1(n))(t) + S(lambda n: a2*x2(n))(t)
