from math import factorial
print("Welcome to task 1!")
while True:
    try:
        n = int(input("Enter some 'n' for (a+b)^n: "))
        break
    except ValueError:
        print("It must be integer!")

def binom(n, k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def pascal_triangle(n):
    for i in range(0, n+1):
        row=[]
        for k in range(0, i+1):
            c = binom(i,k)
            row.append(c)
        yield row


print("Pascal`s triangle: ")
for row in pascal_triangle(n):
    print(" ".join(map(str, row)))