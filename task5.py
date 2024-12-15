print('Завдання 5:')

while True:
    try:
        object1 = input('Enter the name of the first object: ')
        if object1.isdigit():    # Перевірка, чи введене значення - цифра. Якщо так, цикл повертається в початок, і буде повторюватись доки не введуться букви
            print('Enter a word, not a number')
            continue  
        elif object1.isalpha():     # Перевірка, чи є введенне значення буквою. Якщо так, цей цикл завершується.
            print(f"You entered the first object: {object1}")
            break 
        else:
            print('Enter a valid word without numbers or special characters.')
    except ValueError:
        print('Enter a word, not a number.')

while True:
    try:
        object2 = input('Enter the name of the second object: ')
        if object2.isdigit():
            print('Enter a word, not a number')
            continue  
        elif object2.isalpha():
            print(f"You entered the second object: {object2}")
            break  
        else:
            print('Enter a valid word without numbers or special characters.')
    except ValueError:
        print('Enter a word, not a number.')

while True:
    try:
        object3 = input('Enter the name of the third object: ')
        if object3.isdigit():
            print('Enter a word, not a number')
            continue  
        elif object3.isalpha():
            print(f"You entered the first object: {object3}")
            break  
        else:
            print('Enter a valid word without numbers or special characters.')
    except ValueError:
        print('Enter a word, not a number.')

while True:
    try:
        object4 = input('Enter the name of the fourth object: ')
        if object4.isdigit():
            print('Enter a word, not a number')
            continue  
        elif object4.isalpha():
            print(f"You entered the second object: {object4}")
            break 
        else:
            print('Enter a valid word without numbers or special characters.')
    except ValueError:
        print('Enter a word, not a number.')

while True:
  list = [object1, object2, object3, object4] # Задаємо список
  if list == [object1, object2, object3, object4]:  # Якщо список дійсно має такі об'єкти, результат виводиться на екран
   print('\n', list[0])
   print('\n', list[0],  'and', list[1])
   print('\n', list[0] + ',', list[1], 'and', list[2])
   print('\n', list[0] + ',', list[1] + ',', list[2], 'and', list[3])
   break # Завершення циклу
 