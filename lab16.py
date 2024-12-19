print("Welcome to task!")
from math import sqrt

def check(a,b,c):
    try:
        if (a+b)>c and (b+c)>a and (a+c)>b:
            if a>0 and b>0 and c>0:
                return True
        else:
            print("You can`t make a triangle from these segments")
    except ValueError:
        print("You should write only digits!")

def triangle_ineq(func):
    def inner(a,b,c):
        if check(a,b,c)==True:
            return func(a,b,c)        
        else:
            return ("Incorrect values!")  
    return inner  

@triangle_ineq
def area_calculation(a, b, c):
    p = (a+b+c)/2
    s = p*(p-a)*(p-b)*(p-c)
    return f"S = {round(sqrt(s), 3)}"

while True:
    try:
        a = float(input("Input a: "))
        b = float(input("Input b: "))
        c = float(input("Input c: "))
        print(area_calculation(a, b, c))
        break
    except ValueError:
        print("Wrong digits!")    