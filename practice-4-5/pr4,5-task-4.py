print('PAYROLL REPORT\n'
      'SALARY TABLE\n'
      '--------------------------------------------------------------------------------------------------------------------')
salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
increased_salary_list =[]
indexation_list = []
for item in range(0,len(salary_list)):#creating two lists for task
    increased_salary = round(salary_list[item]*1.3,2)
    indexation = round(increased_salary - salary_list[item],2)
    increased_salary_list.append(increased_salary)
    indexation_list.append(indexation)
print('|NUMBER OF EMPLOYEES  |SALARY(BEFORE INDEXATION)(UAN)|SALARY(AFTER INDEXATION)(UAN) |AMOUNT OF INDEXATION(UAN)     |\n'#creating a table for output date
      '--------------------------------------------------------------------------------------------------------------------'
)
for item in range(0,len(salary_list)):
    print('|',item+1,end='                   |')
    if len(str(salary_list[item])) == 4:
        print(salary_list[item],end='                          |')
    elif len(str(salary_list[item])) == 3:
        print(salary_list[item],end='                           |')
    elif len(str(salary_list[item])) == 2:
        print(salary_list[item],end='                            |')
    else:
        print(salary_list[item],end='                         |')
    if len(str(increased_salary_list[item])) == 4:
        print(increased_salary_list[item],end='                          |')
    else:
        print(increased_salary_list[item],end='                         |')
    if len(str(indexation_list[item])) == 4:
        print(indexation_list[item],end='                          |')
    elif len(str(indexation_list[item])) == 3:
        print(indexation_list[item],end='                           |')
    else:
        print(indexation_list[item],end='                         |')
    print('\n------------------------------------------------------------------------------------------------------------------')