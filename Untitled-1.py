print("Welcome to lab 10 task 1!\n")

salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

def apply(x, funct):
    result = funct(x)
    return result

def salary_function(listt):
    new_salary_list = list(map(lambda n: round(n + n * 0.30, 2), listt))
    difference_list = list(map(lambda n, m: round(n - m, 2), new_salary_list, listt))
    for i in range(len(listt)):
        print(listt[i], new_salary_list[i], difference_list[i])

print("Salary table:")
apply(salary_list, salary_function)
print("\nDone!")