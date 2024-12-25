def cons(head, tail=None):
    if tail is None:
        return [head]
    return [head] + tail

def get_head(pair):
    return pair[0]

def get_tail(pair):
    return pair[1:] if len(pair) > 1 else []

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

def sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum(lst[1:])

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')