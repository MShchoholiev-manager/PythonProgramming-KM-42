import factorial
import exp_root
import logarithm

def num_check(text, type = 'int'):
    while(True):
        try:
            num = int(input(text)) if type == "int" else float(input(text))
        except ValueError:
            print('Invalid input. Try again.')
            continue
        else:
            break

    return num


def positive_num_check(text, type = 'int', is_only_positive = False):
    while(True):
        try:
            num = num_check(text, type)
            assert num >= 0 if not is_only_positive else num >0
        except AssertionError:
            print('Invalid input. Try again.')
            continue
        else:
            break

    return num

def base_check (text, type = 'int', is_only_positive = False):
    while(True):
        try:
            num = positive_num_check(text, type, is_only_positive)
            assert num != 1
        except AssertionError:
            print('Invalid input. Try again.')
            continue
        else:
            break

    return num

def valid_check(text, l1st, type = 'int'):
    while (True):
        try:
            num = num_check(text, type)
            assert num in l1st
        except AssertionError:
            print('Invalid input. Try again.')
            continue
        else:
            break

    return num

def main():
    while(True):
        print(
        f"{'-' * 40}",
        f"{'MATH CALCULATOR':^40}",
        f"{'-' * 40}",
        "1. FACTORIAL.",
        "2. EXPONENTIATION AND ROOT.",
        "3. LOGARITHM.",
        "0. EXIT.",
        f"{'-' * 40}",
        sep = '\n'
        )

        choice = valid_check('What category of functions do you want to use? ', [0, 1, 2, 3])

        match choice:
            case 0:
                print('Come back soon!')
                break
            case 1:
                print(
                f"{'-' * 40}",
                f"{'FACTORIAL FUNCTION':^40}",
                f"{'-' * 40}",
                sep = '\n'
                )
                num = positive_num_check('Enter the number for factorial: ')
                print(f'Factorial of {num} is {factorial.fact(num)}')
            case 2:
                print(
                f"{'-' * 40}",
                f"{'EXPONENTIATION AND ROOT FUNCTIONS':^40}",
                f"{'-' * 40}",
                "1. SQUARE OF A NUMBER.",
                "2. CUBE OF A NUMBER.",
                "3. SQUARE ROOT OF A NUMBER.",
                "4. CUBE ROOT OF A NUMBER.",
                f"{'-' * 40}",
                sep='\n'
                )

                choice_exp = valid_check('What function do you want to use? ', [1, 2, 3, 4])

                match choice_exp:
                    case 1:
                        num = num_check('Enter the number for square exponentiation: ', 'float')
                        print(f'Square of {num} is {exp_root.exp2(num)}')
                    case 2:
                        num = num_check('Enter the number for cube exponentation: ', 'float')
                        print(f'Cube of {num} is {exp_root.exp3(num)}')
                    case 3:
                        num = positive_num_check('Enter the number for square root: ', 'float')
                        print(f'Square root of {num} is {exp_root.root2(num)}')
                    case 4:
                        num = num_check('Enter the number for cube root: ', 'float')
                        print(f'Cube root of {num} is {exp_root.root3(num)}')
            case 3:
                print(
                f"{'-' * 40}",
                f"{'LOGARITHM FUNCTIONS':^40}",
                f"{'-' * 40}",
                "1. LOGARITHM TO BASE B.",
                "2. COMMON (DECIMAL) LOGARITHM.",
                "3. NATURAL LOGARITHM.",
                f"{'-' * 40}",
                sep='\n'
                 )

                choice_log = valid_check('What function do you want to use? ', [1, 2, 3])

                match choice_log:
                    case 1:
                        a = positive_num_check('Enter the number for logarithm: ', 'float', True)
                        b = base_check('Enter the number for base: ', 'float', True)
                        print(f'Logarithm of {a} to base {b} is {logarithm.log(a, b)}')
                    case 2:
                        a = positive_num_check('Enter the number for common logarithm: ', 'float', True)
                        print(f'Common logarithm of {a} is {logarithm.lg(a)}')
                    case 3:
                        a = positive_num_check('Enter the number for natural logarithm: ', 'float', True)
                        print(f'Natural logarithm of {a} is {logarithm.ln(a)}')

if __name__ == '__main__':
    main()