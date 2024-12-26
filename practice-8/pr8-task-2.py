import math
def check_float(text):#check type of input
      while (True):
            try:
                  num = float(input(text))
            except ValueError as ve:
                  print(ve, 'Your coefficient must be a number (consist of only digits)!', sep='\n')
                  continue
            else:
                  break
      return num
while(True):
    a = check_float('Enter the coefficient a of the quadratic equation: ')
    b = check_float('Enter the coefficient b of the quadratic equation: ')    
    c = check_float('Enter the coefficient c of the quadratic equation: ')
    try:
        x1 = round(((-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2*a)),2)
        x2 = round(((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2*a)),2)
        x_set = {x1, x2}#solution
    except ValueError as ve:#
        print(ve, 'The square of b must be equal to or greater than the expression 4ac for the equation to have a solution!', sep='\n')
        continue
    except ZeroDivisionError as zde:#root of a negative number
        print(zde, 'The coefficient a cannot be zero!', sep='\n')
        continue
    else:
        print('Solution of a quadratic equation: ', x_set)
        break