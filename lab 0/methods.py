import math

''' ПРОСТО ФУНКЦИИ'''
def dividing_a_string_by_a_number(stroka, a):
    if a != 0: stroka = [i/a for i in stroka]
    else: print('деление на ноль', stroka, 'and' ,a)
    return stroka


def rearranging_strings(array,s1,s2):
    array[s1],array[s2] = array[s2],array[s1]
    return array


def adding_strings(str1,str2,a):
    str2 = [i - a * j for i,j in zip(str2,str1)]
    return str2


def upper_matrix(array):
    U = [i*1 for i in array]
    n = len(array)
    for i in range(n): 
        U[i] = dividing_a_string_by_a_number(U[i],U[i][i])   
        for j in range(i+1,n): 
            U[j] = adding_strings(U[i],U[j], U[j][i])
    return U


def search_x(array_):
    upper_array =  upper_matrix(array_)
    found_values = []
    # sum = 0
    m = len(upper_array)
    for i in upper_array[-1::-1]:
        sum = 0
        if found_values != []:
            for j in range(len(found_values)):
                c = i[m -(j+1)]
                xk = found_values[j]
                sum = sum + xk*c
                # print(sum)
        x = i[-1] - sum
        found_values.append(x)
    found_values.reverse()
    return found_values


def determinate(array):
    U = array
    n = len(array)
    det = 1
    for i in range(n):
        if U[i][i] != 0:
            det = det*U[i][i]
            U[i] = dividing_a_string_by_a_number(U[i],U[i][i])   
            for j in range(i+1,n): 
                U[j] = adding_strings(U[i],U[j], U[j][i])
        else:
            print('blyaa')           
    return det

'''----------------------------------------------------------'''

def norm(x): return sum(i**2 for i in x)**(0.5)

def matrix_vector_multiplication(A, Z):
    n = len(A)
    Z_ = [0]*n
    for i in range(n):
        for j in range(n): Z_[i] = Z_[i] + A[i][j]*Z[j]
    return Z_

def the_power_method(array,Z,eps):
    A = [i*1 for i in array]

    lamb = []
    k = 0
    z = [Z]
    h = []
    while True:
        z.append(matrix_vector_multiplication(A,z[-1]))
        h.append(norm(z[-1])/norm(z[-2]))
        k +=1
        if k>1 and abs(h[-1]-h[-2]) < eps: break
    # print(k, " - iterations")
    return h[-1]


'''ВТОРОЕ. метод интерполяции.'''

'''1е L_k'''

def uniform_grid_(Lmax, n):
    s = [0]
    for i in range(1,n+1): s.append( i*(Lmax/n))
    return s


''' 2е найти зн ф-ций с помощью м.Гаусса'''

def A_LiE_(A,setkaa_i):
    A_LiE = A
    n = len(A)
    print(setkaa_i, 'setka')
    for i in range(n): A_LiE[i][i] = A_LiE[i][i] - setkaa_i
    return A_LiE


def dividing_a_string_by_a_number(stroka, a):
    if a != 0: stroka = [i/a for i in stroka]
    else: print('деление на ноль', stroka, 'and' ,a)
    return stroka


def rearranging_strings(A,s1,s2):
    A[s1],A[s2] = A[s2],A[s1]
    return A


def adding_strings(str1,str2,a):
    str2 = [i - a * j for i,j in zip(str2,str1)]
    return str2


def determinate(array):
    U = [i*1 for i in array]
    n = len(U)
    det = 1
    for i in range(n):
        if U[i][i] != 0:
            det = det*U[i][i]
            U[i] = dividing_a_string_by_a_number(U[i],U[i][i])   
            for j in range(i+1,n): 
                U[j] = adding_strings(U[i],U[j], U[j][i])
        else:
            print('blyaa')           
    return det


def array_minus_eigenvalues(array, lamb):
    arr = [i*1 for i in array]
    n = len(arr)
    for i in range(n): arr[i][i] = arr[i][i] - lamb
    return arr


def function_k(A,setk):
    m = len(setk)
    f = [determinate(array_minus_eigenvalues(A, i)) for i in setk]
    return f


'''3e строим интерполяционный полином Лагранжа'''

def wr1(array_xk,array_yk, n):
    for k in range(n):
        for i in range(n):
            if i != k and i != n-1:
                print("((x - ", array_xk[i], ")/(", array_xk[k] - array_xk[i],")) * ", end ='')
            elif i != k and i==n-1: print("((x - ", array_xk[i], ")/(", array_xk[k] - array_xk[i],"))*", end = "")

        if k!= n-1: print( array_yk[k], "+", end ="")
        elif k == n-1: print( array_yk[k],)

    return


'''РЕШЕНИЕ НЕЛИНЕЙНОГО УР'''

def met_del(f, a, b, eps):
    h1 = a
    h2 = b  
    while True:
        if f(h1)*f(h2) < 0:
            h_sr = (h1 + h2)*0.5
            if f(h1)*f(h_sr)< 0: h2 = h_sr
            else: h1 = h_sr
            if abs(f(h_sr))< eps or abs(a-b) < eps: return h_sr
        else: 
            # print('huipidoras chmo loh idi nahui')
            return None


def method(f,a,b,eps):
    # step = (b-a)/(10**(2))
    step = 1
    p1 = a
    p2 = p1 + step
    k = 0
    X = [] # массив значений 
    while True:
        # print('[',p1, ';', p2,']' )
        x = met_del(f, p1, p2, eps)
        # print(x, "its x")
        X.append(x)
        p1 = p2
        p2 = p1 + step
        k = k+ 1
        if p2 > b or k >= 100: return [i for i in X if i ]


'''ТРЕТЬЕ НАХОЖДЕНИЕ СОБСТВЕННЫХ ВЕКТОРОВ'''

def matrix_expansion(array,z0):
    new_array = [i*1 for i in array]
    # print(id(array), id(new_array) ,' b ', id(array[0]), id(new_array[0]))
    for i in range(len(z0)): new_array[i].append(z0[i])
    return new_array


def norm_vector(vec): 
    return [i/ norm(vec) for i in vec]


# def search_eigenvectors(array,z0,L,eps):
#     res =[]
#     for i in L:
#         xx = search_x(array_minus_eigenvalues(matrix_expansion(array,z0), i + eps))
#         xx = norm_vector(xx)
#         res.append(xx)
#     return res


def examination_one(array,vect,L,eps):
    arr = [i*1 for i in array]
    vec1 = matrix_vector_multiplication(arr,vect)
    vec2 = [i*L for i in vect]
    result = [i - j for i,j in zip(vec1,vec2)]
    # print(result)
    if norm(result) < eps:
        # print(result, " good") 
        return True
    else: return False


def search_vector(array, L, eps):
    x = [1]*2
    while True:
        A = [i*1 for i in array]
        x = norm_vector(search_x(array_minus_eigenvalues(matrix_expansion(A,x), L+eps)))
        if examination_one(array,x,L,eps) == True: return x


def search_all_vectors(array, L, eps):
    vectors = []
    n = len(array)
    for i in range(n): 
        vectors.append(search_vector(array, L[i], eps))
        # print(vectors)

    return vectors


def scalar_multiplication_of_vectors(vec1, vec2):
    result = sum([i*j for i,j in zip(vec1, vec2)])
    return result


def examination_two(vect,eps):
    n = len(vect)
    kronecker_delta =[]
    for i in range(n):
        res = []
        for j in range(n): res.append(scalar_multiplication_of_vectors(vect[i], vect[j]))
        kronecker_delta.append(res)
    return kronecker_delta
