import numpy as np

years = np.arange(1900, 2020+4, 1)
years_list = years


def find_leap_years(years_list):
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False
    
    return list(map(int, filter(is_leap_year, years)))
leap_years = find_leap_years(years)
print("Leap years:", leap_years)


def days_in_month(year, month, leap_years):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year in leap_years:
        month_days[1] = 29

    return month_days[month - 1]

while True:

    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (four digits): "))
    
    if 1 <= month <= 12 and 1900 <= year <=2023:
        days = days_in_month(year, month, leap_years)
        print(f"Number of days on month {month} of year {year}: {days}")
        break
    else:
        print("Enter the number according to the specified rules")
   





