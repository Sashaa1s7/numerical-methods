import math 
import numpy as np

from methods import *

z0 = [1]*10
eps = 10**(-5)

# здесь просто матрицу вытаскиваю из файла
file = open('Labrab1.txt')

array = []
with open("Labrab1.txt") as file:
    k = False
    for row in file:
        if row == "\n": k = False
        if "Вариант 5" in row: k = False
        if k == True:
            # print(row) 
            array.append(row.split()) 
            array[-1] = [float(n) for n in array[-1]]
            # print(array1[-1])
        if "Вариант 4" in row: k = True



max_L = the_power_method(array,z0,eps)
setka = uniform_grid_(max_L, len(array))
f_k = function_k(array,setka)


with  open("Lagranj.txt", "w+") as file2:
    def wr(array_xk,array_yk, n):

        for k in range(n):
            for i in range(n):
                if i != k and i != n-1:
                    file2.writelines(["((x - ", str(array_xk[i]), ")/(", str(array_xk[k] - array_xk[i]),")) * "])
                elif i != k and i==n-1: file2.writelines(["((x - ", str(array_xk[i]), ")/(", str(array_xk[k] - array_xk[i]),")) *"])

            if k!= n-1: file2.writelines([ str(array_yk[k]), " + "])
            elif k == n-1: file2.writelines([ str(array_yk[k])])
        return
    wr(setka, f_k, 11)


def f(x): 
    return ((x - 1.0399567669498104)/(-1.0399567669498104)) * ((x - 2.079913533899621)/(-2.079913533899621)) * ((x - 3.1198703008494313)/(-3.1198703008494313)) * ((x - 4.159827067799242)/(-4.159827067799242)) * ((x - 5.199783834749052)/(-5.199783834749052)) * ((x - 6.239740601698863)/(-6.239740601698863)) * ((x - 7.279697368648673)/(-7.279697368648673)) * ((x - 8.319654135598483)/(-8.319654135598483)) * ((x - 9.359610902548294)/(-9.359610902548294)) * ((x - 10.399567669498104)/(-10.399567669498104)) *10556423.233948652 + ((x - 0)/(1.0399567669498104)) * ((x - 2.079913533899621)/(-1.0399567669498104)) * ((x - 3.1198703008494313)/(-2.079913533899621)) * ((x - 4.159827067799242)/(-3.1198703008494313)) * ((x - 5.199783834749052)/(-4.159827067799242)) * ((x - 6.239740601698863)/(-5.199783834749052)) * ((x - 7.279697368648673)/(-6.239740601698863)) * ((x - 8.319654135598483)/(-7.279697368648673)) * ((x - 9.359610902548294)/(-8.319654135598483)) * ((x - 10.399567669498104)/(-9.359610902548294)) *332397.70646873355 + ((x - 0)/(2.079913533899621)) * ((x - 1.0399567669498104)/(1.0399567669498104)) * ((x - 3.1198703008494313)/(-1.0399567669498104)) * ((x - 4.159827067799242)/(-2.079913533899621)) * ((x - 5.199783834749052)/(-3.1198703008494313)) * ((x - 6.239740601698863)/(-4.159827067799242)) * ((x - 7.279697368648673)/(-5.199783834749052)) * ((x - 8.319654135598483)/(-6.239740601698863)) * ((x - 9.359610902548294)/(-7.279697368648673)) * ((x - 10.399567669498104)/(-8.319654135598483)) *-19577.412441814125 + ((x - 0)/(3.1198703008494313)) * ((x - 1.0399567669498104)/(2.079913533899621)) * ((x - 2.079913533899621)/(1.0399567669498104)) * ((x - 4.159827067799242)/(-1.0399567669498104)) * ((x - 5.199783834749052)/(-2.079913533899621)) * ((x - 6.239740601698863)/(-3.1198703008494313)) * ((x - 7.279697368648673)/(-4.159827067799242)) * ((x - 8.319654135598483)/(-5.199783834749052)) * ((x - 9.359610902548294)/(-6.239740601698863)) * ((x - 10.399567669498104)/(-7.279697368648673)) *3431.0175284270663 + ((x - 0)/(4.159827067799242)) * ((x - 1.0399567669498104)/(3.1198703008494313)) * ((x - 2.079913533899621)/(2.079913533899621)) * ((x - 3.1198703008494313)/(1.0399567669498104)) * ((x - 5.199783834749052)/(-1.0399567669498104)) * ((x - 6.239740601698863)/(-2.079913533899621)) * ((x - 7.279697368648673)/(-3.1198703008494313)) * ((x - 8.319654135598483)/(-4.159827067799242)) * ((x - 9.359610902548294)/(-5.199783834749052)) * ((x - 10.399567669498104)/(-6.239740601698863)) *-1106.2370548970996 + ((x - 0)/(5.199783834749052)) * ((x - 1.0399567669498104)/(4.159827067799242)) * ((x - 2.079913533899621)/(3.1198703008494313)) * ((x - 3.1198703008494313)/(2.079913533899621)) * ((x - 4.159827067799242)/(1.0399567669498104)) * ((x - 6.239740601698863)/(-1.0399567669498104)) * ((x - 7.279697368648673)/(-2.079913533899621)) * ((x - 8.319654135598483)/(-3.1198703008494313)) * ((x - 9.359610902548294)/(-4.159827067799242)) * ((x - 10.399567669498104)/(-5.199783834749052)) *565.9430070473034 + ((x - 0)/(6.239740601698863)) * ((x - 1.0399567669498104)/(5.199783834749052)) * ((x - 2.079913533899621)/(4.159827067799242)) * ((x - 3.1198703008494313)/(3.1198703008494313)) * ((x - 4.159827067799242)/(2.079913533899621)) * ((x - 5.199783834749052)/(1.0399567669498104)) * ((x - 7.279697368648673)/(-1.0399567669498104)) * ((x - 8.319654135598483)/(-2.079913533899621)) * ((x - 9.359610902548294)/(-3.1198703008494313)) * ((x - 10.399567669498104)/(-4.159827067799242)) *-430.5596428173011 + ((x - 0)/(7.279697368648673)) * ((x - 1.0399567669498104)/(6.239740601698863)) * ((x - 2.079913533899621)/(5.199783834749052)) * ((x - 3.1198703008494313)/(4.159827067799242)) * ((x - 4.159827067799242)/(3.1198703008494313)) * ((x - 5.199783834749052)/(2.079913533899621)) * ((x - 6.239740601698863)/(1.0399567669498104)) * ((x - 8.319654135598483)/(-1.0399567669498104)) * ((x - 9.359610902548294)/(-2.079913533899621)) * ((x - 10.399567669498104)/(-3.1198703008494313)) *472.62583295761505 + ((x - 0)/(8.319654135598483)) * ((x - 1.0399567669498104)/(7.279697368648673)) * ((x - 2.079913533899621)/(6.239740601698863)) * ((x - 3.1198703008494313)/(5.199783834749052)) * ((x - 4.159827067799242)/(4.159827067799242)) * ((x - 5.199783834749052)/(3.1198703008494313)) * ((x - 6.239740601698863)/(2.079913533899621)) * ((x - 7.279697368648673)/(1.0399567669498104)) * ((x - 9.359610902548294)/(-1.0399567669498104)) * ((x - 10.399567669498104)/(-2.079913533899621)) *-735.2003581670839 + ((x - 0)/(9.359610902548294)) * ((x - 1.0399567669498104)/(8.319654135598483)) * ((x - 2.079913533899621)/(7.279697368648673)) * ((x - 3.1198703008494313)/(6.239740601698863)) * ((x - 4.159827067799242)/(5.199783834749052)) * ((x - 5.199783834749052)/(4.159827067799242)) * ((x - 6.239740601698863)/(3.1198703008494313)) * ((x - 7.279697368648673)/(2.079913533899621)) * ((x - 8.319654135598483)/(1.0399567669498104)) * ((x - 10.399567669498104)/(-1.0399567669498104)) *1516.1966338811415 + ((x - 0)/(10.399567669498104)) * ((x - 1.0399567669498104)/(9.359610902548294)) * ((x - 2.079913533899621)/(8.319654135598483)) * ((x - 3.1198703008494313)/(7.279697368648673)) * ((x - 4.159827067799242)/(6.239740601698863)) * ((x - 5.199783834749052)/(5.199783834749052)) * ((x - 6.239740601698863)/(4.159827067799242)) * ((x - 7.279697368648673)/(3.1198703008494313)) * ((x - 8.319654135598483)/(2.079913533899621)) * ((x - 9.359610902548294)/(1.0399567669498104)) * -156.55030743868014

eigenvalues = method(f,0,max_L+1, 10**(-4))

xx = search_all_vectors(array, eigenvalues , eps)
print(xx)


# print(examination_two(xx,eps))
