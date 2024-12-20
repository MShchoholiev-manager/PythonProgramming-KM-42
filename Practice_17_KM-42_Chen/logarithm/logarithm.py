import math

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Base 'a' must be > 0 and != 1; 'b' must be > 0.")
    return math.log(b, a)

def ln(b):
    if b <= 0:
        raise ValueError("'b' must be > 0 for natural logarithm.")
    return math.log(b)

def lg(b):
    if b <= 0:
        raise ValueError("'b' must be > 0 for common logarithm.")
    return math.log10(b)