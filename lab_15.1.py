print('Welcome to lab 15 task 1!')
while True:
    try:
        n = int(input('Enter the exponent of the binomial (non-negative integer): '))
        if n < 0:
            print('Please enter a non-negative integer.')
            continue
        break
    except ValueError:
        print('Invalid input. Please enter a valid non-negative integer.')

def pascal_triangle(n):
    row = [1]
    for _ in range(n + 1):
        yield row
        row = [1] + [sum(pair) for pair in zip(row, row[1:])] + [1]

for row in pascal_triangle(n):
    print(*row)