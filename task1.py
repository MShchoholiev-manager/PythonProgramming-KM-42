salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

def newlist(list1):
    salary = list(map(lambda i: round(i * 1.30, 2), list1))
    list2 = list(map(lambda d: d, list1))
    difference = list(map(lambda i, d: round((i-d),2), salary, list2))
    for k in range(len(list1)):
        print(list1[k], salary[k], difference[k])

def apply(x, func):
    return func(x)

print('Salary table:')
apply(salary_list, newlist)