#Code

def cons(head, tail =  None):
    if tail == None:
        tail = []
        
    tail[:0] = [head]
    return tail

#Test

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')

#Code

def sum(lst):
    if len(lst) == 0:
        return 0
    
    elif len(lst) == 1:
        return lst[0]
    
    else:
        result = lst[0] + sum(lst[1:])
        return result

#Test

print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')