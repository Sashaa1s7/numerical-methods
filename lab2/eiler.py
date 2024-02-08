def m_e2(f,y0,dy0, h, a, b):

    xk = []
    dyk = []
    yk = []
    xk.append(a)
    dyk.append(dy0)
    yk.append(y0)

    while True:
        ddyk = f(xk[-1],yk[-1],dyk[-1])
        dyk.append(dyk[-1] + h * ddyk)
        yk.append(yk[-1] + h * dyk[-1])
        xk.append(xk[-1] + h)

        if xk[-1] >= b: break
    return [xk, dyk, yk]


def m_e(f,y0,dy0, h, a, b):
    xk= a
    dyk= dy0
    yk= y0

    while True:
        ddyk = f(xk, yk, dyk)
        dyk = dyk + h * ddyk
        yk= yk + h * dyk
        xk= xk + h

        if xk >= b: break
    return yk


def m_e3(f,y0,dy0, h, a, b):

    xk = []
    dyk = []
    yk = []
    xk.append(a)
    dyk.append(dy0)
    yk.append(y0)

    R3 = []

    while True:
        if xk[-1] >= b: break
        ddyk = f(xk[-1],yk[-1],dyk[-1])
        dyk.append(dyk[-1] + h * ddyk)
        yk.append(yk[-1] + h * dyk[-1])


        xk.append(xk[-1] + h)

        R3.append([xk[-1], yk[-1]])


    return R3