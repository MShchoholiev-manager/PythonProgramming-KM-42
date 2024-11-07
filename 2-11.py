def rrange(begin, end, step = 1):
    if step == 0:
        return 1

    if step < 0 and begin > end:
        list1 = [begin, ]
        if begin == end - 1:
            return list1
        list1 += rrange(end + 1, begin, step)
        list1 = list(filter(lambda i: i / step == int(i / step), list1))
        list1.sort(reverse=True)
        return list1 

    else:
        list1 = [begin, ]
        if begin == end - 1:
            return list1
        if begin > end and step > 0:
            return []
        list1 += rrange(begin + 1, end, step)
        list1 = list(filter(lambda i: i / step == int(i / step), list1))
        return list1 
    

# ПЕРЕВІРКА

x = rrange(1, 10)
y = rrange(10, 1, -1)
z = rrange(10, 1, 1)
print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')

    