def q(t):
    # negative t
    tn = np.array([i for i in t if i < 0])
    # positive t
    tp = np.array([i for i in t if i >= 0])

    neg = x_i(tn)
    pos = 2*x_o(tp) + x_i(-tp)
    return np.concatenate((neg, pos))

