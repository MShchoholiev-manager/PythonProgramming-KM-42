import numpy as np
import itertools

#-------------------------------------------------------------------------------------------------------

def random_matrix(dim):
    """
    Функція генерує матрицю розміром (dim) на (dim) з цілих чисел у діапазоні від 0 до 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

#-------------------------------------------------------------------------------------------------------

def gen_perm(n):
    """
    Генерує усі можливі перестановки від 1 до заданої n.
    """
    t = list(itertools.permutations(range(n)))
    return t

#-------------------------------------------------------------------------------------------------------

def calc(matrix, perm):
    """
    Обчислює добуток елементів зпираючись на введену перестановку.
    """
    calc = 1
    for i in range(len(perm)):
        calc = calc * (matrix[i][perm[i]])
    return calc

#-------------------------------------------------------------------------------------------------------

def calc_deter(matrix):
    """
    Обчислює визначник матриці за правилом перестановок.
    """
    n = len(matrix)
    perms = gen_perm(n)
    det_matrix = 0

    #ПЕРЕВІРКА НА ПАРНІСТЬ ЧИ НЕПАРНІСТЬ

    for p in perms:
    
        swaps = 0
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    swaps += 1
        
        parity = (-1) ** swaps
        det_matrix += (parity * calc(matrix, p))
        
    return det_matrix

#-------------------------------------------------------------------------------------------------------
while True:
    # ЗАДАННЯ ПАРАМЕРУ (dim)
    dim = input("Введіть розмір квадратної матриці або введіть exit щоб вийти: ")
    
    # ВИМКНЕННЯ
    if dim == "exit" or "EXIT":
        break

    # РОЗМІР МАТРИЦІ
    dim = int(dim)
    matrix = random_matrix(dim)
    print("Вигляд згенерованої матриця:")
    print(matrix)

    # МЕТОД ПЕРЕСТАНОВКИ
    deter = calc_deter(matrix)
    print("Результа за правилом перестановок:", deter)

    # ПЕРЕВІРКА ЧЕРЕЗ NUMPY
    np_deter = np.linalg.det(matrix)
    print("Перевірка за допомогою numpy:", round(np_deter, 0))
