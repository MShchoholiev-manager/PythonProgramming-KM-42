def fact(n):
    if n < 0:
        raise ValueError("Input must be a natural number (n >= 0).")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result