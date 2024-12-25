import math

def check(a, b, c):
    return all(isinstance(side, (float)) and side > 0 for side in (a, b, c))

def triangle_ineq(func):
    def wrapper(a, b, c):
        if not check(a, b, c):
            raise ValueError("All sides of the triangle must be positive numbers.Try again.")
        if a + b > c and a + c > b and b + c > a:
            return func(a, b, c)
        else:
            raise ValueError("You can`t make a triangle from these segments.")
    return wrapper

@triangle_ineq
def area_calculation(a, b, c):
    p = (a + b + c) / 2 
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


while True:
    try:
        a = float(input("Enter a value of parametr a: "))
        b = float(input("Enter a value of parametr b: "))
        c = float(input("Enter a value of parametr c: "))
        area = area_calculation(a, b, c)
        print(f"Area of a triangle: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    break