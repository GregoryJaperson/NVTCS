def matrix_transpose(A):
    M = []
    for i in range(len(A[0])):
        M.append(list())
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M

def scalar_multiplication(A, z):
    g = [[] * n for n in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            g[i].append(A[i][j])
            g[i].append(A[i][j])
    return g

def matrix_addition(A, B):
    a, b = len(A), len(B[0])
    S = [[0] * b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            S[i][j] = A[i][j] + B[i][j]
    return S

def matrix_substraction(A, B):
    a, b = len(A), len(B[0])
    S = [[0] * b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            S[i][j] = A[i][j] - B[i][j]
    return S


def mul_matr(A, B):
    a, b, c = len(A), len(A[1]), len(B[1])
    S = [[0] * c for _ in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                S[i][k] = S[i][k] + A[i][j] * B[j][k]
    return S
