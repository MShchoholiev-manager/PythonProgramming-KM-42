while True:
    try:
        inp = int(input('Enter an integer > 0 for Newton\'s binomial:'))
        if inp < 0:
             raise ValueError('You need enter an integer > 0')
        break
    except ValueError as ve:
        print(f'ValueError: {ve}. Try again.')
    
def pascal_triangle(inp):
    for n in range(inp + 1):
            row = [1]
            for k in range(1, n + 1):
                row.append(row[-1] * (n - k + 1) // k)
            yield row
                
for row in pascal_triangle(inp):
     print(" ".join(map(str, row)))