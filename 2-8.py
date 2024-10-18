import math

x1 = ()
x2 = ()
x = [x1, x2]
print("ax^2 + bx + c = 0")
try:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    disc = b**2 - 4*a*c
    x1 = float(-b-math.sqrt(disc))/(a*2)
    x1 = round(x1, 2)
    x2 = float(-b+math.sqrt(disc))/(a*2)
    x2 = round(x2, 2)
    if x1 == x2:
        print(f"x = {x1}")
    if x1 != x2:
        print(f"x1 = {x1}\nx2 = {x2}")
except ValueError:
    print("Помилка! Введено невірний символ або дискрімінант від'ємний!")
except ZeroDivisionError:
    print("На нуль диліти не можна!")
except Exception:
    print("Помилка!")