import numpy as np
import itertools
def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.(for the correct operation of the program, 
    the function displays the tuple of the created matrix and the dimension)
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix, dim
def num_check(text):
    """
    The function checks the entered data to be
    a positive integer.
    """
    i = True
    while(i):
        try:
            num = int(input(text))
            assert num > 0
        except ValueError:
            print('Oops...Dimension can only be a number!')
            continue
        except AssertionError:
            print('Oops...Dimension can only be a positive number!')
            continue
        i = False
    return num
def permutation(tuple):
    """
    The function creates a list of permutations. 
    """
    matrix, dim = tuple 
    array =''
    for i in range(1,dim + 1):
        array += f'{i}'
    global t
    t = list(itertools.permutations(array))
    return matrix
def list_of_product(matrix):
    """
    The function creates a list of elements that are
    the product of matrix elements (the column number is determined by permutations)
    """
    all_products = list()
    for i in range(len(t)):#creates a list from the lists of items that we will multiply
        product =  list()
        for j in range(len(matrix)):
            product.append(matrix[j][int(t[i][j]) - 1].item())
        all_products.append(product) 
    result_of_multiplication = list()
    for r in range(len(all_products)):#creates a list of products
        element = 1
        for r1 in all_products[r]:
            element *= r1
        result_of_multiplication.append(element)
    return result_of_multiplication
def sum(a_list):
    """
    The function sums the products in order
    to obtain the sign determined by the number of inversions
    """
    sign_of_product = list()
    for i in range(len(t)):
        count_of_inversion = 0
        for j in range(len(t[i]) - 1):
            for k in range(j + 1, len(t[i])):
                if int(t[i][j]) > int(t[i][k]):
                    count_of_inversion += 1
        if count_of_inversion % 2 == 0:
            sign_of_product.append(1)
        else:
            sign_of_product.append(-1)
    determinant = 0
    for s in range(len(a_list)):
        determinant += a_list[s] * sign_of_product[s]
    print(f'Determinant of the matrix {max(t[0])} x {max(t[0])}: {determinant}')
sum(list_of_product(permutation(random_matrix(num_check('Enter the dimension of the matrix: ')))))