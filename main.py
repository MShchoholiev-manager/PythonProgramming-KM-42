from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():

    while True:
        print("\nMenu:")
        print("1) Factorial")
        print("2) Exponentiation")
        print("3) Root")
        print("4) Logarithm")
        print("0) Exit")

        try:
            task = int(input('Enter a number of task in menu:'))

            if task == 1:
                n = int(input("Enter an integer:"))
                try:
                    print("Factorial:", fact(n))
                except ValueError as ve:
                    print(ve)
            elif task == 2:
                x = float(input('Enter a number:'))
                print("Squared number:", exp2(x))
                print("Cubed number:", exp3(x))
            elif task == 3:
                x = float(input('Enter a number:'))
                print('Square root:', root2(x))
                print('Cube root:', root3(x))
            elif task == 4:
                a = int(input('Enter a base for log:'))
                b = int(input('Enter a number b:'))
                print(f'log({a}, {b}):', log(a, b))
                print(f'ln({b}):', ln(b))
                print(f'lg({b}):', lg(b))
            elif task == 0:
                print("You exit the program.")
                break
            else:
                print('\nUncorrect number. Try again.')
        except ValueError as  ve:
            print(ve)


if __name__ == '__main__':
    main()