print('\nКурс "Програмування на мові Python" \n')
print("Практичні зайняття №4-5 \n")
print('Тема: "Перші програми на Python. Введення та виведення даних. Інструкція if. Цикли. Робота зі списками" \n')
print("Завдання №4")

salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
for i in range(0, 7):
    salary = salary_list[i]
    indexation = salary * 0.3
    newsalary = salary + indexation
    print(salary, round(indexation, 2), round(newsalary, 2), "\n")