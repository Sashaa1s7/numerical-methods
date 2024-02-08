import scipy.integrate as integrate
import matplotlib.pyplot as plt
import dop

import math

a = 0.2
b = 0.4
c = 0.4
L = 1.0
d = 0.15
h = 0.2
E = 10**19
J = (d* h**3)/12
q = 10**5
R = -(1/(E*J))

# k = 20
def func(x):
    if x >= 0 and x <= a: return R*24000 * x
    if x >= a and x <= a+b: return R*1000*(-2 + 44*x - 50* x**2)
    if x >= a+b and x <= L: return R*16000*(1 - x)


def FF(n):
    f = []
    c = []
    for k in range(n):

        def fi_k(x): return -x**k *(L-x)

        def d_fi_k(x): return -(k*L*(x**(k-1)) - (k+1)*(x**(k)))

        def F(x):
            return func(x)*fi_k(x)

        c_j = []
        for j in range(n):
            def d_fi_j(x): return -(j*L*(x**(j-1)) - (j+1)*(x**(j)))
            def FF(x): return d_fi_k(x)*d_fi_j(x)
            c_j.append(-1*(integrate.quad(FF, 0.0, L)[0]))

        c.append(c_j)
        f.append(integrate.quad(F, 0.0, a)[0] +integrate.quad(F, a, a+b)[0]+integrate.quad(F, a+b, L)[0])

    # print(result)
    return [f, c]


N = 15

# print("это типа f \n", FF(N)[0])

# print("это типа c \n", FF(N)[-1])


alfa = dop.gauss_method(FF(N)[-1], FF(N)[0])
print("a = \n", a)


# дальше нужно найти само решение

def fi_k(x, k): return -x**k *(L-x)

def yn(x, n, alfa):
    y0 = 0
    for i in range(1,n): y0 = y0 + alfa[i-1]*fi_k(x, i)
    return y0


h = 10**(-5)
x = []
y = []
x.append(0)

while True:
    y.append(yn(x[-1], N, alfa))
    x.append(x[-1]+ h)
    if x[-1] > L: break


print("y\n", y)
print("x\n", x)

x.pop()
# plt.plot(hh,maxabs, color = 'g')
plt.plot(x,y, color = 'g')


plt.title("**")
plt.xlabel('x')
plt.ylabel(' y')
plt.show()
