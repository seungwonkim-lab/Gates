intuitiveNANDGATE.pydef NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = w1*x1 + w2*x2
    if tmp >= theta:
        return 1
    elif tmp < theta:
        return 0
