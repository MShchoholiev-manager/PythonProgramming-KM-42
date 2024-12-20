salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

percentage = 0.30

def calculate_salary(salary):
    return round(salary * (1 + percentage))

def calculate_percentage(salary):
    return round(salary * percentage)
# d1 = list(map(lambda i, y: i * (1 + y), x))
#     d2 = list(map(lambda i, y: i * y, x))
# salary_list = x
# salary = y

# print(d1(salary_list, salary))
new_salary = list(map(calculate_salary, salary_list))
percentage_amounts = list(map(calculate_percentage, salary_list))

print("salary table:")

for i in range(len(salary_list)):
    print(f"{salary_list[i]}, {new_salary[i]}, {percentage_amounts[i]}")
