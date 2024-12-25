import numpy as np

years = np.arange(1900, 2024 + 1, 1)

def is_leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def get_leap_years(years):
    return list(filter(is_leap_year, years))

def days_in_month(leap_year_func, month, year):

    is_leap = leap_year_func(year)
    
    if month == 2:
        return 29 if is_leap else 28
    elif month in [4, 6, 9, 11]:
        return 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return "Wrong month."

while True:
    try:
        year = int(input("Enter the year (four-digit integer): "))
        
        if year < 1900 or year > 2024:
            raise ValueError("The year must be between 1900 and 2024 inclusive.")
        
        break

    except ValueError as ve:
        print("ValueError:", ve)

while True:
    try:
        month = int(input("Enter the month number (from 1 to 12): "))
        
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        
        break

    except ValueError as ve:
        print("ValueError:", ve)

leap_years = get_leap_years(years)
print("Leap years in list:", leap_years)

days = days_in_month(is_leap_year, month, year)
print(f"Number of days in month {month} of {year} year: {days}")