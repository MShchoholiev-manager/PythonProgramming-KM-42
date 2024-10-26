import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

#Example of using permutations() method

def sigh(sp):
    """
    Обчислює знак перестановки.
    
    Параметри:
        sp (list): Перестановка у вигляді списку чисел.
        
    Повертає:
        int: 1, якщо перестановка парна, -1, якщо непарна.
    """
    inversions = 0
    for i in range(len(sp)):
        for j in range(i + 1, len(sp)):
            if sp[i] > sp[j]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def dobut(t, matrix):
    """
    Обчислює добутки елементів матриці для кожної перестановки з урахуванням її знаку.
    
    Параметри:
        t (list): Список перестановок.
        matrix (list of lists): Квадратна матриця.
        
    Повертає:
        list: Список добутків для кожної перестановки, з урахуванням їх знаків.
    """
    sp_result = []
    for i in t:
        result = 1
        for g in i: 
            result = result * matrix[i.index(g)][g]
        
        sp_result.append(result * sigh(i))
    return sp_result


def rearrangement(matrix):
    """
    Створює список усіх можливих перестановок індексів для заданої матриці.
    
    Параметри:
        matrix (list of lists): Квадратна матриця.
        
    Повертає:
        list: Список усіх перестановок індексів матриці.
    """
    sp = []
    for i in range(len(matrix[0])):
        sp.append(i)
    t = list(itertools.permutations(sp))
    return t


def sum(det):
    """
    Обчислює суму елементів списку.
    
    Параметри:
        det (list): Список чисел.
        
    Повертає:
        int: Сума всіх елементів у списку.
    """
    total_sum = 0
    for i in det:
        total_sum += i
    return total_sum

while True:          
    try: 
        size = int(input("Розмір матриці: "))
        if size < 0: 
            print("Число повинно бути невід'ємним")
        else:
            break
    except:
        print("Введіть число")
a = random_matrix(size)
print(a)
print("Детермінант", (sum(dobut(rearrangement(a), a))))
print(np.linalg.det(a))

