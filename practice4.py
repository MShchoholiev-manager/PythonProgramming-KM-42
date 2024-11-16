print("Welcome to task 4!")
salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
increase = 0.30
indexation_list = []
new_salary_list = []
for salary in salary_list:
 indexation = salary * increase
 new_salary = indexation + salary
 indexation_list.append(round(indexation, 2))
 new_salary_list.append(round(new_salary, 2))
    
print("Salary table: ")
for n in range(len(salary_list)):
 print(salary_list[n], new_salary_list[n], indexation_list[n])