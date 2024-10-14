print('Завдання 4: Розрахунок заробітної плати\n')

difference_list = [] #empty list for differences in salaries

salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7] #original salary

salary_list_new = [] #empty list for new salaries

rise = 0.30 #30% rise

for salary in salary_list: #calculates the difference and salaries
    summa = salary * rise
    salary_new = salary + summa
    salary_list_new.append(round(salary_new, 2))
    difference_list.append(round(summa, 2))
    
print('Salary table:')

for i in range(len(salary_list)): #prints salary, new salary and difference
    print(salary_list[i], salary_list_new[i], difference_list[i])

print('\nDone')