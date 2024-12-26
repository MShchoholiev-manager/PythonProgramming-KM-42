import numpy as np

years = np.arange(1900, 2020+4, 1)


def leap_year(years):
    """
    Returns a list of leap years from a given range of years.
    """
    check = list(filter(lambda i: (i % 4 == 0) and ((i % 100 != 0) or (i % 400 == 0)), years))
    check = [int(i) for i in check]
    return check


def number_of_a_day(leap_year, month, year):
    """
    Calculates the number of days in a specific month of a given year.
    """
    months = ("January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"
    )
    day = 0
    if month in ([int(i) for i in range(1, 8, 2)] + [int(i) for i in range(8, 13, 2)]):
        day = 31
    elif month == 2:
        if year in leap_year(years):
            day = 29
        else:
            day = 28
    else:
        day = 30
    print(f'The number of days in {months[month - 1]} {year} is {day}')
    

def check_int(text):
    """
    Prompts the user to enter an integer value, handling invalid inputs.
    """
    while(True):
        try:
                num = int(input(text))
        except ValueError:
                print('Oops...Only integers can be entered!')
                continue
        else:
                break
    return num


def check_assert(max, min, text):
    """
    Prompts the user to enter an integer within a specified range.
    """
    while(True):
        try:
            num = check_int(text)
            assert (num <= min) and (num >= max)
        except AssertionError:
            print('Oops...This option is not possible!')
            continue
        else:
            break
    return num


month = check_assert(1, 12, 'Enter the numeric month number: ')
year = check_assert(1900, 2023, 'Enter the year: ')
number_of_a_day(leap_year, month, year)