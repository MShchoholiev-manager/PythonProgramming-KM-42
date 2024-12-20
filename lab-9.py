import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def permutations():
    """
    The fuction for permutations
    """
    t = list(itertools.permutations('123', 3))

def calculate_product(matrix, perm):
    """
    The function for multiplication
    """
    product = 1
    for i in range(len(perm)):
        product *= matrix[i][perm[i]]
    return product

def calculate_determinant(matrix):
    """
    Calculates the determinant of a matrix using permutation rules.
    
    :param matrix: Square matrix.
    :return: Determinant of the matrix.
    """
    n = matrix.shape[0]
    perms = permutations(n)
    determinant = 0
    
    for perm in perms:
        product = calculate_product(matrix, perm)
        sign = (-1) ** sum(1 for j in range(n) for k in range(j + 1, n) if perm[j] > perm[k])
        determinant += sign * product
    
    return determinant

if __name__ == "__main__":
    while True:
        try:
            size = int(input("Enter the dimension of the square matrix (a positive integer): "))
            if size > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please try again.")
    
    matrix = random_matrix(size)
    print("Matrix:")
    print(matrix)
    
    
    determinant = calculate_determinant(matrix)
    print("Matrix determinant:", determinant)
    
    
    np_det = np.linalg.det(matrix)
    print("Verification using np.linalg.det:", np_det)


