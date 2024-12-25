import math
print('Solving of quadratic equation ax^2 + bx + c')
while True:
    try:
        a = float(input("Enter value of \'a\': "))
        if a == 0:
            print("Value of \'a\' can not be less than zero. Try again.")
            continue
    except ValueError as ve:
        print(ve)
        continue

    try:
        b = float(input("Enter value of \'b\': "))
    except ValueError as ve:
        print(ve)
        continue

    try:
        c = float(input("Enter value of \'c\': "))
    except ValueError as ve:
        print(ve)
        continue

    try:
     discriminant = b**2 - 4*a*c
     if discriminant < 0:
      print("discriminant less than zero. Try again.")
      continue
    except Exception as exc:
       print(exc)

    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    print(f"Quadratic equation roots: \nx1 = {root1} \nx2 = {root2}")
    break  