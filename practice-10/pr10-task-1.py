salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
salary_indexation = list(map(lambda i: round(i * 1.3, 2), salary_list))
amount_of_indexation = list(map(lambda i: round(i * 0.3, 2), salary_list))
print('Salary table:')
for i in range(len(salary_list)):
    print(f'{salary_list[i]}',
          f'{salary_indexation[i]}',
          f'{amount_of_indexation[i]}'
    )