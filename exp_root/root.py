import math
def root2(x):
    if x < 0:
        raise ValueError ('Uncorrect value. Try again')
    return math.sqrt(x)

def root3(x):
    return x ** 1/3