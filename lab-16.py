import math

def triangle_ineq(func):
    def wrapper(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("The sides must be positive numbers.")
        
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("A triangle with such sides cannot be constructed (triangle inequalities are not fulfilled).")
        
        return func(a, b, c)
    
    return wrapper

@triangle_ineq
def area_calculation(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

try:
    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the first side of the triangle: "))
    c = float(input("Enter the first side of the triangle: "))
    
    area = area_calculation(a, b, c)
    print(f"Area of ​​the triangle: {area}")
except ValueError as e:
    print(f"Error: {e}")
