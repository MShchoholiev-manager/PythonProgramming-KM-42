def root2(x):
    if x < 0:
        raise ValueError("Input must be a positive number for square root.")
    return x ** 0.5

def root3(x):
    return x ** (1/3)