print("Welcome to the Lab 8 task 2!")
print("Searching for the roots of the quadratic equation ax^2+bx+c=0")
import math 
while True:
    try:
        a = float(input("Please enter a value of the quadratic coefficient(a): "))
        b = float(input("Please enter a value of the linear coefficient(b): "))
        c = float(input("Please enter a value of the free term(c): "))
        D = b ** 2 - 4 * a * c
        if D < 0:
            print(f"The equation {a}x^2+{b}x+c=0 doesn't have any roots because the discriminant is less than zero.")
            break
        elif D == 0:
            if a == 0:
                x = -c / b
                print(f"The discriminant is equal to {D}. The equation {b}x+c=0 has one root: {round(x, 3)}")
                break
            else:
                x = (-b) / 2 * a
                (f"The discriminant is equal to {D}. The equation {a}x^2+{b}x+c=0 has one root: {round(x, 3)}")
                break
        else:
            if a == 0:
                x = -c / b
                print(f"The discriminant is equal to {D}. The equation {b}x+c=0 has one root: {round(x, 3)}")
                break
            else:
                x1 = (-b - math.sqrt(D)) / (2 * a)
                x2 = (-b + math.sqrt(D)) / (2 * a)
                print(f"The discriminant is equal to {D}. The equation {a}x^2+{b}x+c=0 has two roots: x1 = {round(x1, 3)}, x2 = {round(x2, 3)}")
                break
    except ValueError as exp:
        print(f"The error is {exp}!")

print("Done.")
