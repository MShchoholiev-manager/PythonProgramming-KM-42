print('Завдання 2: Grades.\n')

while True:
    try:
        R = int(input('Enter your rating score(from 0 to 100): '))
        if R < 0:
            print('You must enter a positive number!')
        elif R >= 0 and R < 60:
            print('Your grade is "Unsatisfactory":(')
        elif R >= 60 and R < 65:
            print('Your grade is "Marginal":(')
        elif R >= 65 and R < 75:
            print('Your grade is "Satisfactory":|')
        elif R >= 75 and R < 85:
            print('Your grade is "Good":)')
        elif R >= 85 and R < 95:
            print('Your grade is "Very good":)')
        elif R >= 95 and R <= 100:
            print('Your grade is "Excelent"!:)')
        elif R > 100:
            print('Enter a number that does not exceed 100')
            continue
        else:
            break
        break
    except ValueError:
        print('You should enter integer!')

print('Done')
