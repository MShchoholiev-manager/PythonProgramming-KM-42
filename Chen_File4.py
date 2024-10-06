salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

new_salarylist = []

increase_list = []

for salary in salary_list:
    increase = round(salary * 0.30 , 2)
    new_salary = round(salary + increase , 2)
    new_salarylist.append(new_salary)
    increase_list.append(increase)

print("Salary table:\n"
      f'Original: {salary_list}\n'
      f'New: {new_salarylist}\n'
      f'Increases: {increase_list}')
