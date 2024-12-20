import math

a = float(input("Enter number a:"))
b = float(input("Enter number b:"))
c = float(input("Enter number c:"))


try:
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("There are no solutions")
    else:
        x1 = (b * (-1) + D ** 0.5) / (2 * a)
        x2 = (b * (-1) - D ** 0.5) / (2 * a)
        print(" x1 =", x1, "\n", "x2 =", x2)
except Exception as exp:
    print("Error =", exp)

