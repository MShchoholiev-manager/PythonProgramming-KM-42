import numpy as np
import itertools

print("Welcome to lab 9!")

while True:
    try:
        dim = int(input("Set the matrix dimensions: "))
        if dim <= 0:
            raise ValueError("Dimension must be a positive integer.")
        break 
    except ValueError as exp:
        print(exp)

def random_matrix(dim):
    """
    Generates a dim x dim array of integers between 0 and 10.
    """
    return np.random.randint(10, size=(dim, dim))

def permutations_matrix(dim):
    """
    Generates permutations of indices and their signs.
    """
    permutations_with_sign = []
    for perm in itertools.permutations(range(dim)):
        inversions = sum(1 for i in range(len(perm)) for j in range(i + 1, len(perm)) if perm[i] > perm[j])
        sign = 1 if inversions % 2 == 0 else -1
        permutations_with_sign.append((perm, sign))
    return permutations_with_sign

def product_matrix(matrix, perm):
    """
    Computes the product of matrix elements for a given permutation.
    """
    product = 1
    for i in range(len(perm)):
        product *= matrix[i, perm[i]]
    return product

def calculate_determinant(matrix):
    """
    Calculates the matrix determinant using permutations.
    """
    dim = len(matrix) 
    permutations_with_sign = permutations_matrix(dim)
    return sum(sign * product_matrix(matrix, perm) for perm, sign in permutations_with_sign)

matrix = random_matrix(dim)
det = calculate_determinant(matrix)

print("Matrix:")
print(matrix)
print("Determinant of the matrix:", det)

print("Done!")

