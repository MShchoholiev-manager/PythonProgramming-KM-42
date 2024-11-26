def permutations(n):
    if n == 1:
        yield [1] 
    else:
        for perm in permutations(n - 1):
            for i in range(n):
                yield perm[:i] + [n] + perm[i:]

print(list(permutations(3)))
