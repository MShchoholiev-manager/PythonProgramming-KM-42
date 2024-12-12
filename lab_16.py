from math import sqrt

print('\n\tWelcome to lab 16.')
print('  Calculation of the triangle area.')

while True:
    try:
        a = float(input('Enter the length of side "a"(positive): '))
        if a <= 0:
            raise ValueError('the value can not be negative!')
        break
    except ValueError as e:
        print(f'The promlem is "{e}", please try again.')

while True:
    try:
        b = float(input('Enter the length of side "b"(positive): '))
        if b <= 0:
            raise ValueError('the value can not be negative!')
        break
    except ValueError as e:
        print(f'The promlem is "{e}", please try again.')

while True:
    try:
        c = float(input('Enter the length of side "c"(positive): '))
        if c <= 0:
            raise ValueError('the value can not be negative!')
        break
    except ValueError as e:
        print(f'The promlem is "{e}", please try again.')
        
def check(a,b,c):
    if (a+b)>c and (b+c)>a and (a+c)>b:
        return True
    else:
        return False

def triangle_ineq(func):
    def inner(a,b,c):
        if check(a,b,c)==True:
            return func(a,b,c)        
        else:
            return 'You can`t make a triangle from these segments. The sum of two sides should exceed the third.'
    return inner  

@triangle_ineq
def area_calculation(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return f'S = {round(sqrt(s), 3)}'


print(area_calculation(a, b, c))
print('Done!\n')