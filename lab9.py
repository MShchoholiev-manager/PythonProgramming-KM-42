import numpy as np
from itertools import permutations

def main():
    """
    Main function for calculating the determinant of a matrix using the permutation rule.
    """

    def random_matrix(dim):
        """
        Generates a square matrix of size dim x dim with random integers from 0 to 10.
        """
        matrix = np.random.randint(10, size=(dim, dim))
        return matrix

    def calculate_determinant(matrix):
        """
        Calculates the determinant of a matrix using the permutation rule.
        """
        n = len(matrix)
        
        def permutation_product(perm):
            """
            Calculates the product of elements for a given permutation, taking the sign into account.
            """
            product = 1
            inversions = 0
            for i in range(n):
                product *= matrix[i][perm[i]]
                for j in range(i + 1, n):
                    if perm[i] > perm[j]:
                        inversions += 1
            return (-1) ** inversions * product

        return sum(permutation_product(perm) for perm in permutations(range(n)))

    try:
        n = int(input("Enter the matrix dimension (an integer): "))
        if n <= 0:
            print("Dimension mustn't be less or equal to 0.")
            return

        matrix = random_matrix(n)
        print("Generated matrix:")
        print(matrix)

        determinant = calculate_determinant(matrix)
        print("Determinant of matrix:", determinant)

    except ValueError:
        print("Enter an integer.")

main()