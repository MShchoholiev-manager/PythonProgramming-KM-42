from math import factorial

def gen(n):
    for i in range(n + 1):
        
        row = (factorial(i) // (factorial(k) * factorial(i - k)) for k in range(i + 1))
        yield row  

n = 5
binom_gen = gen(n)

for _ in range (n+1):
    line = next(binom_gen)
    print(" ".join(map(str, line)))