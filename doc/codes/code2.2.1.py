def z(t):
    # negative t
    tn = np.array([i for i in t if i < 0])
    # positive t
    tp = np.array([i for i in t if i >= 0])

    neg = 2*x_e(tn) - x_r(-tn)
    pos = x_r(tp)
    return np.concatenate((neg, pos))

