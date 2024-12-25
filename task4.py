print('Завдання 4:')

salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7] # Список, що заданий умовою
while True:
 new_salaries = [] # Створення нових списків для заповнення новими елементами
 indexation_values = []
 for salary in salary_list:
    indexation = round(salary * 0.30, 2)  # Індексація заробітніх плат з урахуванням округлення до сотих

    new_salary = round(salary + indexation, 2)  # Нова заробітня плата з урахуванням округлення до сотих
    
    indexation_values.append(indexation) # Введення нових значень у створенні пусті списки
    new_salaries.append(new_salary)
 print("Salary table:")

 for i in range(len(salary_list)):
    print('\n'f"{salary_list[i]} {new_salaries[i]} {indexation_values[i]}") # Виведення результату 
 break