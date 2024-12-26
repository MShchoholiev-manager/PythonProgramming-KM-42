import math

def check(text):
    while(True):
        try:
            num = int(input(text))
            assert num >= 0
        except ValueError:
            print('This is not a valid option. The number must be integer and non-negative.')
            continue
        except AssertionError:
            print('This is not a valid option. The number must be integer and non-negative.')
            continue
        else:
            break
    
    return num

num = check('Enter the degree of a polynomial: ')
print(f"Pascal's triangle from 0 to {num}:")
for i in range(num + 1):
    bin_coeff = (math.factorial(i)//(math.factorial(j)*math.factorial(i-j)) for j in range(i + 1))#Generator expression
    for j in bin_coeff:
        print(j, end = ' ')
    print()