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

step = 0.0001
osh = [0.01]
res = [eiler.m_e3(fun,tetta0 + osh[-1],dtetta0, step, t0, tk)]


for i in range(10):
    k = eiler.m_e3(fun,tetta0+osh[-1],dtetta0, step, t0, tk)
    res.append(k)
    osh.append(osh[-1]/5)


print(len(res[-1]))
print(len(res[-2]))

maxabs = []
for k in range(1,len(res)):
    ras = max([(abs(res[k-1][i][1] - res[k][i][1])) for i in range(len(res[-1])-1)])
    maxabs.append(ras)
print(len(maxabs))
osh.pop(0)
print(len(osh))

# osh.pop()
# osh = [math.log(osh[i]) for i in range(len(osh))]

# maxabs = [math.log(maxabs[i]) for i in range(len(maxabs))]
print(osh)
print(maxabs)


# plt.plot(hh,maxabs, color = 'g')
plt.plot(osh,maxabs, color = 'b')


plt.title("Line")
plt.xlabel('ln(h)')
plt.ylabel(' ln(maxabs)')
plt.show()