try:
    r = int(input("Your mark in 'R': "))
    if r < 0 or r > 100:
        print("Incorrect value")
    else:
        if r >= 95:
            print("Excellent")
        elif r >= 85 and r < 95:
            print("Very good")
        elif r >= 75 and r < 85:
            print("Good")
        elif r >= 65 and r < 75:
            print("Satisfactory")
        elif r >= 60 and r < 65:
            print("Marginal")
        else:
            print('Unsatisfactory')
except:
    print("Please input number")