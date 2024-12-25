import math
def log(a, b):
    if not a >0 and a != 1:
        return ValueError('Base must be greater than 0 and != 1')
    if not b > 0:
        return ValueError('b must be > 0')
    return math.log(a, b)

def ln(b):
    if not b > 0:
        return ValueError('Parameter must be greater than zero')
    return math.log(b)

def lg(b):
    if not b > 0:
        return ValueError('Parameter must be greater than zero')
    return math.log10(b)