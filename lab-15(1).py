def generate_pascals_triangle(n):
    triangle = []
    
    for i in range(n + 1):
        row = [1] * (i + 1)  
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]  
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))


try:
    n = int(input("Введіть степінь многочлена: "))
    
    triangle = generate_pascals_triangle(n)
        
    print_pascals_triangle(triangle)

except:
    print("Enter integer")