print("Welcome to task 2!")
while True:
    try:
        R = int(input("Enter your ranking point: "))
        if 95 <= R <= 100:
            print("Excellent!")
            break
        elif 85 <= R < 95:
            print("Very good!")
            break
        elif 75 <= R < 85:
            print("Good!")
            break
        elif 65 <= R < 75:
            print("Satisfactory")
            break
        elif 60 <= R < 65:
            print("Marginal")
            break
        elif 0 <= R < 60:
            print("Unsatisfactory!")
            break
        else:
            print("It is uncorrect! Try again.")
    except ValueError:
     print("Try again! It is cannot contain any letters!")