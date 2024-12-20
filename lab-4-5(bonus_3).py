print('\nКурс "Програмування на мові Python" \n')
print("Практичні зайняття №4-5 \n")
print('Тема: "Перші програми на Python. Введення та виведення даних. Інструкція if. Цикли. Робота зі списками" \n')
print("Завдання №3")

try:
    minute = int(input("\nEnter the number of minutes: "))
    if (minute >= 0) and (minute <= 50):
        print("\nYou need 100 UAH")
    elif (minute > 50) and (minute <= 100): 
        print("\nYou need 150 UAH")
    elif minute > 100:
        print( 150 + 2 * (minute - 100))
    else:
        print("\nError: number < 0\n")
except:
    print("\nIt's not a number!\n")