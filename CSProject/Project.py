from PIL import Image
import math


def image_to_matrix(image_path):
    img = Image.open(image_path)
    w, h = img.size
    matrix = []
    for y in range(h):
        r = []
        for x in range(w):
            pixel = img.getpixel((x, y))
            r.append(pixel)
        matrix.append(r)

    return matrix


def matrix_transpose(A):
    M = []
    for i in range(len(A[0])):
        M.append(list())
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M


def matrix_transpose_short(A):
    return [list(i) for i in zip(*A)]


def scalar_multiplication_tuples(A, z):
    f = [[] * n for n in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(z):
                f[i].append(A[i][j])
    return f


def matrix_to_image(A, output_path):
    h = len(A)
    w = len(A[0]) if h > 0 else 0
    mode = "L" if (type(A[0][0]) == 'int') else "RGB"
    img = Image.new(mode, (w, h))
    for y in range(h):
        for x in range(w):
            img.putpixel((x, y), A[y][x])
    img.save(output_path)

def matrix_addition(A, B):
    a, b = len(A), len(B[0])
    S = [[0] * b for _ in range(a)]
    for i in range(a):
        for j in range(b):
            S[i][j] = A[i][j] + B[i][j]
    return S


A = [[1, 3, 5],[4, 6, 8],[11, 9, 0]]
B = [[1, 3, 5],[4, 6, 8],[11, 9, 0]]


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


def matrix_transpose(A):
    M = []
    for i in range(len(A[0])):
        M.append(list())
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M

def matrix_transpose_short(A):
    return [i for i in zip(*A)]


def scalar_multiplication(A, a):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = A[i][j] * a
    return None


def skew_matrix(A, skew_x, skew_y, bg=(255, 255, 255)):
    h, w = len(A), len(A[0])

    new_w = int(w + skew_x * h)
    new_h = int(h + skew_y * w)
    new_m = [[bg for _ in range(new_w)] for _ in range(new_h)]

    for i in range(h):
        for j in range(w):
            new_i = int(i + skew_y * j)
            new_j = int(j + skew_x * i)
            if 0 <= new_i < new_h and 0 <= new_j < new_w:
                new_m[new_i][new_j] = A[i][j]
    return new_m


def rotate_matrix_angle(A, a, bg=(255, 255, 255)):
    a_r = math.radians(a)
    h, w = len(A), len(A[0])
    cos_r, sin_r = math.cos(a_r), math.sin(a_r)
    new_w = int(abs(w * cos_r) + abs(h * sin_r))
    new_h = int(abs(w * sin_r) + abs(h * cos_r))
    new_m = [[bg for _ in range(new_w)] for _ in range(new_h)]
    xo, yo = w / 2, h / 2
    cx_new, cy_new = new_w / 2, new_h / 2
    for i in range(new_h):
        for j in range(new_w):
            x_old = (j - cx_new) * cos_r + (i - cy_new) * sin_r + xo
            y_old = -(j - cx_new) * sin_r + (i - cy_new) * cos_r + yo
            if 0 <= int(x_old) < w and 0 <= int(y_old) < h:
                new_m[i][j] = A[int(y_old)][int(x_old)]
    return new_m



image = image_to_matrix("hell.png")
j= skew_matrix(image, 1 , 0)
matrix_to_image(j, "image.png")

