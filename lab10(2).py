import numpy as np

# Generate a list of years from 1900 to 2024
years = np.arange(1900, 2025, 1)

def leap_years(years):
    # Filter and return leap years
    return list(filter(lambda i: (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0), years))

def month_days(month, year, leap_year_list):
    day30 = [4, 6, 9, 11]  # Months with 30 days
    day31 = [1, 3, 5, 7, 8, 10, 12]  # Months with 31 days

    if month in day31:
        print("There are 31 days in month")  # 31-day month
    elif month in day30:
        print("There are 30 days in month")  # 30-day month
    elif month == 2:
        if year in leap_year_list:
            print("There are 29 days in month")  # Leap year February
        else:
            print("There are 28 days in month")  # Non-leap year February
    else:
        print("Unindicated!")  # Invalid month

def apply(func1, func2, year, month, years):
    leap_year_list = func1(years)  # Get leap years
    # Output whether the year is leap or not
    if year in leap_year_list:
        print(f"The year {year} is a leap year")  # Leap year message
    else:
        print(f"The year {year} is not a leap year")  # Non-leap year message
    
    return func2(month, year, leap_year_list)  # Call month_days

# Input handling
while True:
    try:
        years_input = int(input("Enter the year (1900-2024): "))  # Year input
        if 1900 <= years_input <= 2024:
            while True:
                try:
                    month_input = int(input("Enter the month (1-12): "))  # Month input
                    if 1 <= month_input <= 12:
                        break
                    else:
                        print("You entered incorrect month!")  # Invalid month message
                except ValueError:
                    print("Enter the correct value!")  # Value error message
            break
        else:
            print("You entered incorrect year!")  # Invalid year message
    except ValueError:
        print("Enter the correct value!")  # Value error message

# Apply the functions
apply(leap_years, month_days, years_input, month_input, years)  # Execute
