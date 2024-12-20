print('\nКурс "Програмування на мові Python" \n')
print("Практичні зайняття №4-5 \n")
print('Тема: "Перші програми на Python. Введення та виведення даних. Інструкція if. Цикли. Робота зі списками" \n')
print("Завдання №2")

try:
    R = int(input("Enter grade: "))
    if (R >= 95) and (R <= 100):
        print("\nExcellent\n")
    elif (R >= 85) and (R < 95):
        print("\nVery good\n")
    elif (R >= 75) and (R < 85):
        print("\nGood")
    elif (R >= 65) and (R < 75): 
        print("\nSatisfactory\n")
    elif (R >= 60) and (R < 65): 
        print("\nMarginal\n")
    elif (R >= 0) and (R < 60):
        print("\nUnsatisfactory\n")
    elif R > 100:
        print("\nError: grade > 100\n")
    else:
        print("\nError: grade < 0\n")
except:
    print("\nIt's not a number!\n")