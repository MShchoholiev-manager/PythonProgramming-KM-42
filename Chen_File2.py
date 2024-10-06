while True:
    score = float(input("Будь ласка, введіть ваші рейтингові бали: "))
    if 100 >= score >= 95: 
        print("Оцінка: Excellent")
        break
    elif 95 > score >= 85:
        print("Оцінка: Very Good")
        break
    elif 85 > score >= 75:
        print("Оцінка: Good")
        break
    elif 75 > score >= 65:
        print("Оцінка: Satisfactory")
        break
    elif 65 > score >= 60:
        print("Оцінка: Marginal")
        break
    elif score < 60: 
        print("Оцінка: Unsatisfactory")
        break
    else:
        print('Помилка, введіть дійсний бал.')