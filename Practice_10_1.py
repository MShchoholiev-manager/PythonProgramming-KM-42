salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
a = list(map(lambda n: round(n * 1.3, 2), salary_list))
b = list(map(lambda first, second: round(first - second, 2), list(map(lambda n: n * 1.3, salary_list)), salary_list))
print("Salary table:")
for i in range(len(salary_list)):
    print(salary_list[i], a[i], b[i])