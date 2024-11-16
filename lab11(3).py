print("Welcome to task 3!")
# ВАШ КОД ТУТ
def Akk(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return Akk(m-1,1)
    else:
        return Akk(m-1, Akk(m,n-1))
        
# ПЕРЕВІРКА

test_pairs = list((m, n) for m in range(0,4) for n in range(0,5))
results = [
    1,  2,  3,  4, 5, 
    2,  3,  4,  5, 6, 
    3,  5,  7,  9, 11,
    5, 13, 29, 61, 125
]
for (m, n), res in zip(test_pairs, results):
    assert Akk(m, n) == res, f'Failed test for (m, n) pair ({m}, {n}): Akk({m}, {n}) = {res}'
print('All tests good!')