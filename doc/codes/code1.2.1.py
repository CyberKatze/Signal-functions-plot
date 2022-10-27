def x1(t): return -ramp(t+2) * unit(-t-1)


def x2(t): return (ramp(2*t+2) - 1) * (unit(t+1)-unit(t))


def x3(t): return unit(t) - unit(t-2)


def x(t): return x1(t)+x2(t)+x3(t)

