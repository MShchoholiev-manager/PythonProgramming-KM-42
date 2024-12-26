while(True):
    try:
        rating_score = float(input('Welcome to KPI calculator!\n'
                                 'Enter your rating score: '))
    except ValueError:
        print("Oops..You've entered the wrong number!Try again.")
        continue
    if (rating_score > 100) or (rating_score < 0):
        print("Oops..You've entered the wrong number!Try again.")
        continue
    elif (rating_score >= 0) and (rating_score < 60):
        print('Your grade is Unsatisfactory!')
    elif (rating_score >= 60) and (rating_score < 65):
        print('Your grade is Marginal!')
    elif (rating_score >= 65) and (rating_score < 75):
        print('Your grade is Satisfactory!')
    elif (rating_score >= 75) and (rating_score < 85):
        print('Your grade is Good!')
    elif (rating_score >= 85) and (rating_score < 95):
        print('Your grade is Very good!')
    else:
        print('Your grade is Excellent!')
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

        