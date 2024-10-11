print("Введіть кількість хвилин:")
minutes = input()
if minutes.isdigit():
    minutes = int(minutes)
    if minutes<=50:
        cost = 100
        print(f"До сплати {cost} гривень")
    if 50<minutes<=100:
        cost = 150
        print(f"До сплати {cost} гривень")
    if minutes>100:
        cost = 150 + 2*(minutes-100)
        print(f"До сплати {cost} гривень")
    if minutes < 0:
        print("Помилка! Спробуйте ввести інше число!")
else:
    print("Помилка! Спробуйте ще раз!")