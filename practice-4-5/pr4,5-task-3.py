import math
while(True):
    try:
        minute = float(input('Calculate your tariff plan!\n'
                             'How many minutes of conversation were there this month? '))
    except  ValueError:
        print("Oops..You've entered the wrong number!Try again.")
        continue
    price = 0
    if minute < 0:
        print("Oops..You've entered the wrong number!Try again.")
        continue
    elif minute <= 50:
        price += 100
        print('Your tariff plan is ', price, " hryvnias")
    elif minute <= 100:
        price += 150
        print('Your tariff plan is ', price, " hryvnias")
    else:
        price += 150 + 2*(math.ceil(minute)-100)
        print('Your tariff plan is ', price, " hryvnias")
    while(True):#Leaving the programm
        try:
            check = int(input('Do you want to leave the programm?\n'
                              'Enter "1" if it is yes\n'
                              'Enter "0" if it is not\n'
                              'Your choice: '))
        except ValueError:
            print("Oops..You've entered the wrong number!Try again.")
            continue
        if (check != 1) and (check != 0):
            print("Oops..You've entered the wrong number!Try again.")
            continue
        break
    match check:
        case 1:
            print('Come back soon!')
            break
        case 0:
            continue
        
    