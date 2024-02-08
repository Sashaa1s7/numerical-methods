import dif

e = dif.e
omega0 = dif.omega


def f1(x, u1, u2):
    return u2

def f2(x, u1, u2):
    return e*(1 - u1 - u1**2)*u2 - omega0**2 * u1

def K1_f1(x, u1,u2):
    return f1(x,u1,u2)

def K1_f2( x,u1,u2):
    return f2(x,u1,u2,)

def K2_f1(x, u1,u2, h):
    return f1(x + h/3,u1 + (h/3) * K1_f1(x,u1,u2),u2 + (h/3) * K1_f2(x,u1,u2))

def K2_f2(x, u1,u2, h):
    return f2(x + h/3,u1 + (h/3) * K1_f1(x,u1,u2), u2 + (h/3) * K1_f2(x,u1,u2))


def K3_f1(x, u1,u2, h):
    return f1(x + (2*h/3),u1 + (2*h/3) * K2_f1(x,u1,u2, h), u2 + (2*h/3) * K2_f2(x,u1,u2, h))

def K3_f2(x, u1,u2, h):
    return f2(x + (2*h/3),u1 + (2*h/3) * K2_f1(x,u1,u2, h), u2 + (2*h/3) * K2_f2(x,u1,u2, h))

def r_k3(y0,dy0, h,a,b):

    u1_k = []
    u2_k = []
    x_k = []
    u1_k.append(y0)
    u2_k.append(dy0)
    x_k.append(a)
    R3 =[]
    while True:
        if x_k[-1] >= b: break
        K1_f1_k = K1_f1(x_k[-1], u1_k[-1], u2_k[-1])
        K2_f1_k = K2_f1(x_k[-1], u1_k[-1], u2_k[-1], h)
        K3_f1_k = K3_f1(x_k[-1], u1_k[-1], u2_k[-1], h)

        K1_f2_k = K1_f2(x_k[-1], u1_k[-1], u2_k[-1])
        K2_f2_k = K2_f2(x_k[-1], u1_k[-1], u2_k[-1], h)
        K3_f2_k = K3_f2(x_k[-1], u1_k[-1], u2_k[-1], h)

        u2_k.append(u2_k[-1] + (h/4)*(K1_f2_k + 3*K3_f2_k ))
        u1_k.append(u1_k[-1] + (h/4)*(K1_f1_k + 3*K3_f1_k ))


        x_k.append(x_k[-1] + h)
        R3.append([x_k[-1], u1_k[-1]])




    # print(x_k)
    # print(u1_k)
    return R3