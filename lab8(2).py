print("Welcome to task 2!")
import math
while True:
 try:
    a = float(input("Enter coefficent a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    D = b **2 - 4 * a * c
    if D == 0:
     x = -b / (2*a)
     print("The discriminant: ", D)
     print("The answer 'x': ", x)
     break
    elif D < 0:
     print("There are no roots roots!")
     break
    else:
     x1 = (-b + math.sqrt(D)) / (2 * a)
     x2 = (-b - math.sqrt(D)) / (2 * a)
     print("The discriminant: ", D)
     print("The first answer 'x1': ", round(x1, 4))
     print("The second answer 'x2': ", round(x2, 4))
     break
 except ZeroDivisionError:
  print("Error: Division by zero! Coefficient 'a' cannot be zero!")
  break
 except ValueError:
  print("Error: Enter valid numbers for a,b,c")


