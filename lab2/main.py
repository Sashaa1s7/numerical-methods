import matplotlib.pyplot as plt
import math
import dif
import eiler
import runge
import runge3

omega = dif.omega
e = dif.e
tetta0 = dif.tetta0
dtetta0 = dif.dtetta0
step = dif.step
t0 = dif.t0
tk = dif.tk

def fun(t,tetta, d_tetta):
    return e*(1 - tetta - tetta**2)*d_tetta - (omega**2)*tetta
    # return - tetta

def index(isk, lst):
    for i in range(len(lst)):
        if isk  in lst[i]:
            return i



# X1 = runge.r_k(tetta0,dtetta0, step,t0,tk)[0]
# DY = runge.r_k(tetta0,dtetta0, step,t0,tk)[1]
# Y = runge.r_k(tetta0,dtetta0, step,t0,tk)[-1]
# X2 = eiler.m_e2(fun,tetta0,dtetta0, step, t0, tk)[0]
# Z = eiler.m_e2(fun,tetta0,dtetta0, step, t0, tk)[-1]


# для эйлера
# print(runge.r_k(tetta0,dtetta0, step,t0,tk)[-1][-1])
# hhh =0.1
# hh =[0.1]
# loghh = [math.log(0.1)]
# resh1 = []
# logr1 =[0]
# resh2 = []
# n = []

# for i in range(10):
#     hh.append(hh[-1]/2)
#     loghh.append(math.log(hh[-1]))
#     # n.append(int((tk - t0)/hh[-1]))
#     resh1.append(abs(eiler.m_e(fun,tetta0,dtetta0, hh[-1],t0,tk) - eiler.m_e(fun,tetta0,dtetta0, hh[-2],t0,tk)))
#     logr1.append(math.log(resh1[-1]))
#     # resh2.append(abs(runge.r_k2(tetta0,dtetta0, hh[-1],t0,tk) - runge.r_k2(tetta0,dtetta0, hh[-2],t0,tk)))


# print(n)
# print(resh1)
# print(resh2)




hh = [0.1]
res = [eiler.m_e3(fun,tetta0,dtetta0, hh[-1], t0, tk)]
res2 = [runge3.r_k3(tetta0,dtetta0, hh[-1],t0,tk)]

for i in range(10):
    hh.append(hh[-1]/2)
    k = eiler.m_e3(fun,tetta0,dtetta0, hh[-1], t0, tk)
    k2 = runge3.r_k3(tetta0,dtetta0, hh[-1],t0,tk)
    res.append(k)
    res2.append(k2)

n = 1
maxabs = []
maxabs2 = []
for k in range(1,len(res2)):
    # ras = max([math.log(abs(res[k-1][n*i][1] - res[k][2*n*i][1])) for i in range(100)])
    ras2 = max([math.log(abs(res2[k-1][i][1] - res2[k][2*i][1])) for i in range(len(res2[k-1])-1)])
    # maxabs.append(ras)
    maxabs2.append(ras2)
    n = n*2



hh.pop()
hh = [math.log(hh[i]) for i in range(len(hh))]

print(hh)
print(maxabs2)


# plt.plot(hh,maxabs, color = 'g')
plt.plot(hh,maxabs2, color = 'b')


plt.title("Line")
plt.xlabel('ln(h)')
plt.ylabel(' ln(maxabs)')
plt.show()